from datasets import load_dataset
from torch.utils.data import DataLoader
import torch
from torch.utils.data import Dataset, DataLoader
from torch import nn
from torch.optim import Adam
from torch.nn.utils.rnn import pad_sequence
from datasets import load_dataset
import itertools
from collections import Counter
from conlleval import evaluate
import datasets

dataset = datasets.load_dataset("conll2003")

word_frequency = Counter(itertools.chain(*dataset['train']['tokens'])) 
word_frequency = {
    word: frequency for word, frequency in word_frequency.items() if frequency >= 3
}
word2idx = {
    word: index for index, word in enumerate(word_frequency.keys(), start=2)
}
word2idx['[PAD]'] = 0
word2idx['[UNK]'] = 1

dataset = (dataset.map(lambda x: {
            'input_ids': [
                word2idx.get(word, word2idx['[UNK]'])
                for word in x['tokens']
            ]}))

tag_freq = Counter(itertools.chain(*dataset['train']['ner_tags']))
tag2idx = {tag: idx for idx, tag in enumerate(sorted(tag_freq.keys()))}
tag2idx['[PAD]'] = len(tag2idx)
dataset = dataset.map(lambda x: {
    'labels': [tag2idx[tag] for tag in x['ner_tags']]
})

dataset = dataset.remove_columns(['pos_tags', 'chunk_tags'])

class NERDataset(Dataset):
    def __init__(self, hf_dataset):
        self.hf_dataset = hf_dataset

    def __len__(self):
        return len(self.hf_dataset)

    def __getitem__(self, idx):
        input_ids = torch.tensor(self.hf_dataset[idx]['input_ids'], dtype=torch.long)
        labels = torch.tensor(self.hf_dataset[idx]['labels'], dtype=torch.long)
        return input_ids, labels

def pad_collate(batch):
    (xx, yy) = zip(*batch)
    xx_pad = pad_sequence(xx, batch_first=True, padding_value=word2idx['[PAD]'])
    yy_pad = pad_sequence(yy, batch_first=True, padding_value=tag2idx['[PAD]'])
    return xx_pad, yy_pad

hf_train_dataset = dataset['train']
train_dataset = NERDataset(hf_train_dataset)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True, collate_fn=pad_collate)

hf_validation_dataset = dataset['validation']
validation_dataset = NERDataset(hf_validation_dataset)
validation_loader = DataLoader(validation_dataset, batch_size=32, shuffle=False, collate_fn=pad_collate)

hf_test_dataset = dataset['test']
test_dataset = NERDataset(hf_test_dataset)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False, collate_fn=pad_collate)

class BiLSTMNERModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim, lstm_hidden_dim, linear_output_dim, num_lstm_layers, lstm_dropout, num_classes):
        super(BiLSTMNERModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.bilstm = nn.LSTM(embedding_dim, lstm_hidden_dim // 2, num_layers=num_lstm_layers, dropout=lstm_dropout, bidirectional=True, batch_first=True)
        self.dropout = nn.Dropout(lstm_dropout)
        self.linear = nn.Linear(lstm_hidden_dim, linear_output_dim)
        self.elu = nn.ELU()
        self.classifier = nn.Linear(linear_output_dim, num_classes)

    def forward(self, x):
        embeddings = self.dropout(self.embedding(x))
        lstm_out, _ = self.bilstm(embeddings)
        linear_out = self.linear(lstm_out)
        elu_out = self.elu(linear_out)
        logits = self.classifier(elu_out)
        return logits

model = BiLSTMNERModel(len(word2idx), 100, 256, 128, 1, 0.33, len(tag2idx))
model.load_state_dict(torch.load('modtask1.pth'))
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

idx2tag = {idx: tag for tag, idx in tag2idx.items() if idx not in [tag2idx['[PAD]']]}
idx2tag[0] = 'O'

model.eval()

test_predictions = []
test_labels = []

with torch.no_grad():
    for batch in test_loader:
        inputs, label_ids = batch
        inputs = inputs.to(device)
        output = model(inputs)
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

original_tags = {0: 'O', 1: 'B-PER', 2: 'I-PER', 3: 'B-ORG', 4: 'I-ORG', 5: 'B-LOC', 6: 'I-LOC', 7: 'B-MISC', 8: 'I-MISC'}

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
