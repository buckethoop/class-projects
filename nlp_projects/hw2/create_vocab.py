import json
from collections import defaultdict

with open('modified_train.json', 'r') as file:
    data = json.load(file)

word_freq = defaultdict(int)
for sequence in data:
    sentence = sequence["sentence"]
    for word in sentence:
        word_freq[word] += 1

word_freq.setdefault("<unk>", 0)

sorted_voc = sorted(word_freq.items(), key=lambda x: (x[0] != "<unk>", -x[1]))
indexed_voc = [(word, index, freq) for index, (word, freq) in enumerate(sorted_voc)]

vocab_size = len(indexed_voc)
print("Size of vocab: ", vocab_size)

with open('vocab.txt', 'w') as file:
    for word, index, freq in indexed_voc:
        file.write(f"{word}\t{index}\t{freq}\n")
