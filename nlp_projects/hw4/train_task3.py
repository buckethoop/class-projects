from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import Dataset, DataLoader
import datasets
from datasets import load_dataset
import itertools
from collections import Counter
import torch
import torch.nn as nn
import torch.nn.functional as F
import math
from conlleval import evaluate

dataset = datasets.load_dataset("conll2003")

tag_freq = Counter(itertools.chain(*dataset['train']['ner_tags']))
tag2idx = {tag: idx for idx, tag in enumerate(sorted(tag_freq.keys()))}
tag2idx['[PAD]'] = len(tag2idx)

word_frequency = Counter(word.lower() for tokens in dataset['train']['tokens'] for word in tokens)
word_frequency = {word: frequency for word, frequency in word_frequency.items() if frequency >= 3}
word2idx = {word: index for index, word in enumerate(word_frequency.keys(), start=2)}
word2idx['[PAD]'] = 0
word2idx['[UNK]'] = 1

dataset = dataset.map(lambda x: {
    'input_ids': [word2idx.get(word.lower(), word2idx['[UNK]']) for word in x['tokens']],
    'labels': [tag2idx[tag] for tag in x['ner_tags']]  
})
dataset = dataset.remove_columns(['pos_tags', 'chunk_tags'])

def create_padding_mask(seq, pad_token_id=0):
    return (seq == pad_token_id).transpose(0, 1)

class NERDataset(Dataset):
    def __init__(self, hf_dataset):
        self.hf_dataset = hf_dataset

    def __len__(self):
        return len(self.hf_dataset)

    def __getitem__(self, idx):
        input_ids = torch.tensor(self.hf_dataset[idx]['input_ids'], dtype=torch.long)
        labels = torch.tensor(self.hf_dataset[idx]['labels'], dtype=torch.long)
        return input_ids, labels

    @staticmethod
    def collate_fn(batch):
        input_ids, labels = zip(*batch)
        input_ids_padded = pad_sequence(input_ids, batch_first=True, padding_value=word2idx['[PAD]'])
        labels_padded = pad_sequence(labels, batch_first=True, padding_value=tag2idx['[PAD]'])
        padding_mask = create_padding_mask(input_ids_padded, pad_token_id=word2idx['[PAD]'])
        return input_ids_padded, labels_padded, padding_mask

hf_train_dataset = dataset['train']
train_dataset = NERDataset(hf_train_dataset)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True, collate_fn=NERDataset.collate_fn)

hf_validation_dataset = dataset['validation']
validation_dataset = NERDataset(hf_validation_dataset)
validation_loader = DataLoader(validation_dataset, batch_size=32, shuffle=False, collate_fn=NERDataset.collate_fn)

hf_test_dataset = dataset['test']
test_dataset = NERDataset(hf_test_dataset)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False, collate_fn=NERDataset.collate_fn)

class PositionalEncoding(nn.Module):
    def __init__(self, embed_size, max_len=5000):
        super(PositionalEncoding, self).__init__()
        pe = torch.zeros(max_len, embed_size)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, embed_size, 2).float() * (-math.log(10000.0) / embed_size))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(1)
        self.register_buffer('pe', pe)

    def forward(self, x):
        x = x + self.pe[:x.size(0), :]
        return x

class TransformerModel(nn.Module):
    def __init__(self, vocab_size, tagset_size, embed_size=128, nhead=8, feedforward_dim=128, nlayers=1, max_seq_length=128):
        super(TransformerModel, self).__init__()
        self.token_embedding = nn.Embedding(vocab_size, embed_size)
        self.positional_encoding = PositionalEncoding(embed_size, max_seq_length)
        encoder_layers = nn.TransformerEncoderLayer(d_model=embed_size, nhead=nhead, dim_feedforward=feedforward_dim)
        self.transformer_encoder = nn.TransformerEncoder(encoder_layers, nlayers)
        self.fc = nn.Linear(embed_size, tagset_size)

    def forward(self, src, src_key_padding_mask):
        token_embedded = self.token_embedding(src)
        src = self.positional_encoding(token_embedded)
        output = self.transformer_encoder(src, src_key_padding_mask=src_key_padding_mask)
        output = self.fc(output)
        return output

model = TransformerModel(len(word2idx), len(tag2idx), embed_size=128, nhead=8,
                         feedforward_dim=128, nlayers=1, max_seq_length=128)

loss_function = nn.CrossEntropyLoss(ignore_index=tag2idx['[PAD]'])
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

idx2tag = {idx: tag for tag, idx in tag2idx.items() if idx not in [tag2idx['[PAD]']]}
idx2tag[0] = 'O'

for epoch in range(20):
    model.train()
    for input_ids, labels, mask in train_loader:
        input_ids, labels, mask = input_ids.to(device), labels.to(device), mask.to(device)
        optimizer.zero_grad()
        outputs = model(input_ids, src_key_padding_mask=mask)
        outputs = outputs.view(-1, outputs.shape[-1])
        labels = labels.view(-1)
        loss = loss_function(outputs, labels)
        loss.backward()
        optimizer.step()

model.eval()
predictions = []
labels = []

with torch.no_grad():
    for batch in validation_loader:
        inputs, label_ids, mask = batch  
        inputs, mask = inputs.to(device), mask.to(device)
        output = model(inputs, src_key_padding_mask=mask)  

        preds = torch.argmax(output, dim=2)
        preds = preds.detach().cpu().numpy()
        label_ids = label_ids.detach().cpu().numpy()

        for i in range(len(preds)):
            seq_preds = []
            seq_labels = []
            for j in range(len(preds[i])):
                if label_ids[i][j] != tag2idx['[PAD]']:
                    seq_preds.append(idx2tag.get(preds[i][j], 'O'))  
                    seq_labels.append(idx2tag.get(label_ids[i][j], 'O'))  
            predictions.append(seq_preds)
            labels.append(seq_labels)

original_tags = {0: 'O', 1: 'B-PER', 2: 'I-PER', 3: 'B-ORG', 4: 'I-ORG', 5: 'B-LOC', 6: 'I-LOC', 7: 'B-MISC', 8: 'I-MISC'}

labels_str_tags = [
    [original_tags.get(label, 'O') for label in label_seq]  
    for label_seq in dataset['validation']['labels']
]

predictions_str_tags = [
    [original_tags.get(pred, 'O') for pred in pred_seq]  
    for pred_seq in predictions
]

labels_flat = list(itertools.chain(*labels_str_tags))
predictions_flat = list(itertools.chain(*predictions_str_tags))

precision, recall, f1 = evaluate(
    labels_flat,
    predictions_flat
)

model.eval()
test_predictions = []
test_labels = []

with torch.no_grad():
    for batch in test_loader:
        inputs, label_ids, mask = batch  
        inputs, mask = inputs.to(device), mask.to(device)
        output = model(inputs, src_key_padding_mask=mask)  

        preds = torch.argmax(output, dim=2)
        preds = preds.detach().cpu().numpy()
        label_ids = label_ids.detach().cpu().numpy()

        for i in range(len(preds)):
            seq_preds = []
            seq_labels = []
            for j in range(len(preds[i])):
                if label_ids[i][j] != tag2idx['[PAD]']:
                    seq_preds.append(idx2tag.get(preds[i][j], 'O'))  
                    seq_labels.append(idx2tag.get(label_ids[i][j], 'O'))  
            test_predictions.append(seq_preds)
            test_labels.append(seq_labels)

test_labels_str_tags = [
    [original_tags.get(label, 'O') for label in label_seq]
    for label_seq in dataset['test']['labels']
]

test_predictions_str_tags = [
    [original_tags.get(pred, 'O') for pred in pred_seq]
    for pred_seq in test_predictions
]

test_labels_flat = list(itertools.chain(*test_labels_str_tags))
test_predictions_flat = list(itertools.chain(*test_predictions_str_tags))

test_precision, test_recall, test_f1 = evaluate(
    test_labels_flat,
    test_predictions_flat
)
