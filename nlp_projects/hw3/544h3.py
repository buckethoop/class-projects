import pandas as pd
import numpy as np
import gensim.downloader as api
import gensim.models
from gensim.test.utils import datapath
from gensim import utils
from gensim.models import KeyedVectors
from sklearn.linear_model import Perceptron
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader, Dataset, SubsetRandomSampler, random_split
import torch.optim as optim

class AmazonReviewDataset(Dataset):

    def __init__(self, file_path, transform=None):
        self.file_path = file_path
        self.transform = transform
        self._load_and_preprocess_data()

    def _load_and_preprocess_data(self):
        try:
            amazon_data = pd.read_csv(self.file_path, sep='\t', on_bad_lines='skip')
        except FileNotFoundError:
            print("File not found. Ensure the correct path is provided.")
            return

        important_fields = ['star_rating', 'review_body']
        amazon_data = amazon_data[important_fields].dropna(subset=['star_rating'])
        amazon_data['review_body'] = amazon_data['review_body'].fillna("")
        amazon_data['Class'] = amazon_data['star_rating'].apply(lambda rating: 0 if rating in [1, 2, 3] else 1)

        review_size = 50000 
        balanced_data = pd.concat([
            amazon_data[amazon_data['Class'] == 0].sample(n=review_size, random_state=4),
            amazon_data[amazon_data['Class'] == 1].sample(n=review_size, random_state=4)
        ], axis=0)

        self.dataframe = balanced_data
        self.dataframe['tokenized_review'] = balanced_data['review_body'].apply(utils.simple_preprocess)

    def __len__(self):
        return len(self.dataframe)

    def __getitem__(self, index):
        tokenized_review = self.dataframe.iloc[index]['tokenized_review']
        label = self.dataframe.iloc[index]['Class']

        if self.transform:
            tokenized_review = self.transform(tokenized_review)
        return tokenized_review, label

#Google
wv = api.load('word2vec-google-news-300')
res = wv.most_similar(positive=['woman', 'king'], negative = ['man'], topn=1)
print("Pretrained Model (Google): ", res)

#Me
data_path = '/content/data.tsv'  # Replace with your actual path
amazon_data = AmazonReviewDataset(data_path)

wrd2vec_reviews = [tokens for tokens, _ in amazon_data]

wrd2vec = gensim.models.Word2Vec(sentences= wrd2vec_reviews, vector_size=300, window=13, min_count=9)

result_own_model = wrd2vec.wv.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
print(f"Trained Model: {result_own_model}")

def avg_word2vec(review, w2v, num_features=300):
    feature_vec = np.zeros((num_features,), dtype='float32')
    n_words = 0
    for word in review:
        if word in w2v:
            n_words += 1
            feature_vec = np.add(feature_vec, w2v[word])
    if n_words:
        feature_vec = np.divide(feature_vec, n_words)
    return feature_vec

data_features = np.array([avg_word2vec(review, wv) for review, _ in amazon_data])
labels = np.array([label for _, label in amazon_data])

X_train, X_test, y_train, y_test = train_test_split(data_features, labels, test_size=0.2, random_state=30)

perc = Perceptron(max_iter=5000)
perc.fit(X_train, y_train)
perc_pred = perc.predict(X_test)

svm = LinearSVC(max_iter=1000)
svm.fit(X_train, y_train)
svm_pred = svm.predict(X_test)


print(f"Perceptron Accuracy (Word2Vec):, {100 * accuracy_score(y_test, perc_pred)}%")
print(f"SVM Accuracy (Word2Vec):, {100 * accuracy_score(y_test, svm_pred)}%")

data_features = [avg_word2vec(review, wv) for review, _ in amazon_data]
labels = [label for _, label in amazon_data]

features_tensor = torch.tensor(data_features, dtype=torch.float32)
labels_tensor = torch.tensor(labels, dtype=torch.long)

dataset = TensorDataset(features_tensor, labels_tensor)
train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size
train_dataset, test_dataset = torch.utils.data.random_split(dataset, [train_size, test_size])

batch_size = 64
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=True)

class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()
        self.fc1 = nn.Linear(300, 50)
        self.fc2 = nn.Linear(50, 5)
        self.fc3 = nn.Linear(5, 2)
        self.relu = nn.ReLU()
        
    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        return x

model = MLP()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
epochs = 100

for epoch in range(epochs):
    for inputs, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

correct = 0
total = 0
with torch.no_grad():
    for inputs, labels in test_loader:
        outputs = model(inputs)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f"Accuracy: {100 * correct / total}%")

def review_to_vector(review, w2v_model, max_len=10):
    vectors = []
    for word in review:
        if word in w2v_model.wv:
            vectors.append(w2v_model.wv[word])
    
    if len(vectors) < max_len:
        vectors.extend([np.zeros(w2v_model.vector_size) for _ in range(max_len - len(vectors))])
    else:
        vectors = vectors[:max_len]
        
    return np.concatenate(vectors, axis=0)

X = [review_to_vector(review, wrd2vec) for review, _ in amazon_data]  # Note: Using wrd2vec model
y = [label for _, label in amazon_data]

X_tensor = torch.tensor(X, dtype=torch.float32)
y_tensor = torch.tensor(y, dtype=torch.long)

dataset = TensorDataset(X_tensor, y_tensor)
train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size
train_dataset, test_dataset = random_split(dataset, [train_size, test_size])

batch_size = 64
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)


class MLP(nn.Module):
    def __init__(self, input_size, hidden_size1=50, hidden_size2=5, output_size=2):
        super(MLP, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size1)
        self.fc2 = nn.Linear(hidden_size1, hidden_size2)
        self.fc3 = nn.Linear(hidden_size2, output_size)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        return x

input_size = wrd2vec.vector_size * 10  # 10 concatenated Word2Vec vectors
mlp_model = MLP(input_size)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(mlp_model.parameters(), lr=0.001)
epochs = 100

for epoch in range(epochs):
    for inputs, labels in train_loader:
        optimizer.zero_grad()
        outputs = mlp_model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

correct = 0
total = 0
with torch.no_grad():
    for inputs, labels in test_loader:
        outputs = mlp_model(inputs)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f"Accuracy: {100 * correct / total}%")

def review_to_vector(review, w2v_model, max_len=10):
    vectors = [w2v_model.wv[word] if word in w2v_model.wv else np.zeros(w2v_model.vector_size) for word in review[:max_len]]
    while len(vectors) < max_len:
        vectors.append(np.zeros(w2v_model.vector_size))
    return np.array(vectors)

X = [review_to_vector(review, wrd2vec) for review, _ in amazon_data]
y = [label for _, label in amazon_data]

X_tensor = torch.tensor(X, dtype=torch.float32)
y_tensor = torch.tensor(y, dtype=torch.long)

dataset = TensorDataset(X_tensor, y_tensor)
train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size
train_dataset, test_dataset = random_split(dataset, [train_size, test_size])

batch_size = 64
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

class RNNModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNNModel, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        h0 = torch.zeros(1, x.size(0), hidden_size).to(x.device)  # Initial hidden state
        out, _ = self.rnn(x, h0)
        out = self.fc(out[:, -1, :])  # Use last sequence output as input to FC layer
        return out

input_size = wrd2vec.vector_size
hidden_size = 10
output_size = 2

model = RNNModel(input_size, hidden_size, output_size)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
epochs = 100

for epoch in range(epochs):
    for inputs, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

correct = 0
total = 0
with torch.no_grad():
    for inputs, labels in test_loader:
        outputs = model(inputs)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f"Accuracy: {100 * correct / total}%")

def review_to_vector(review, w2v_model, max_len=10):
    vectors = [w2v_model.wv[word] if word in w2v_model.wv else np.zeros(w2v_model.vector_size) for word in review[:max_len]]
    while len(vectors) < max_len:
        vectors.append(np.zeros(w2v_model.vector_size))
    return np.array(vectors)

X = [review_to_vector(review, wrd2vec) for review, _ in amazon_data]
y = [label for _, label in amazon_data]

X_tensor = torch.tensor(X, dtype=torch.float32)
y_tensor = torch.tensor(y, dtype=torch.long)

dataset = TensorDataset(X_tensor, y_tensor)
train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size
train_dataset, test_dataset = random_split(dataset, [train_size, test_size])

batch_size = 64
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

class GRUModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(GRUModel, self).__init__()
        self.gru = nn.GRU(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        h0 = torch.zeros(1, x.size(0), hidden_size).to(x.device)  # Initial hidden state
        out, _ = self.gru(x, h0)
        out = self.fc(out[:, -1, :])  # Use last sequence output as input to FC layer
        return out

input_size = wrd2vec.vector_size
hidden_size = 10
output_size = 2

model = GRUModel(input_size, hidden_size, output_size)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
epochs = 100

for epoch in range(epochs):
    for inputs, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

correct = 0
total = 0
with torch.no_grad():
    for inputs, labels in test_loader:
        outputs = model(inputs)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f"Accuracy using GRU: {100 * correct / total}%")

def review_to_vector(review, w2v_model, max_len=10):
    vectors = [w2v_model.wv[word] if word in w2v_model.wv else np.zeros(w2v_model.vector_size) for word in review[:max_len]]
    while len(vectors) < max_len:
        vectors.append(np.zeros(w2v_model.vector_size))
    return np.array(vectors)

X = [review_to_vector(review, wrd2vec) for review, _ in amazon_data]
y = [label for _, label in amazon_data]

X_tensor = torch.tensor(X, dtype=torch.float32)
y_tensor = torch.tensor(y, dtype=torch.long)

dataset = TensorDataset(X_tensor, y_tensor)
train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size
train_dataset, test_dataset = random_split(dataset, [train_size, test_size])

batch_size = 64
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        h0 = torch.zeros(1, x.size(0), hidden_size).to(x.device)  # Initial hidden state
        c0 = torch.zeros(1, x.size(0), hidden_size).to(x.device)  # Initial cell state
        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])  # Use last sequence output as input to FC layer
        return out

input_size = wrd2vec.vector_size
hidden_size = 10
output_size = 2

model = LSTMModel(input_size, hidden_size, output_size)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
epochs = 100

for epoch in range(epochs):
    for inputs, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

correct = 0
total = 0
with torch.no_grad():
    for inputs, labels in test_loader:
        outputs = model(inputs)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f"Accuracy using LSTM: {100 * correct / total}%")