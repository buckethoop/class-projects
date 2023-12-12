import json
import numpy as np

word_index = {}
with open('/Users/buckethoop/Downloads/544_HW2/verification/out/vocab.txt', 'r') as file:
    for line in file:
        word, index = line.split()[:2]
        word_index[word] = int(index)

with open('/Users/buckethoop/Downloads/544_HW2/verification/out/hmm.json', 'r') as file:
    hmm_params = json.load(file) 

with open('/Users/buckethoop/Downloads/544_HW2/data/test.json', 'r') as file:
    original_data = json.load(file)

with open('modified_dev.json', 'r') as file:
    dev_data = json.load(file)

with open('modified_test.json', 'r') as file:
    test_data = json.load(file)

states = set(s for s in hmm_params['initial'].keys())
state_num = len(states)
state_index = {s: i for i, s in enumerate(states)}
trans_matrix = np.zeros((state_num, state_num))
emis_matrix = np.zeros((len(word_index), state_num))

for key, value in hmm_params['transition'].items():
    s, s_prime = key[2:-2].split("','")  # Split the string representation of the tuple
    trans_matrix[state_index[s], state_index[s_prime]] = value

for key, value in hmm_params['emission'].items():
    s, x = key[2:-2].split("','")  # Split the string representation of the tuple
    if x in word_index:
        emis_matrix[word_index[x], state_index[s]] = value

init_st_vector = np.array([hmm_params['initial'][s] for s in states])

def greedyDecode(sentence):
    T = len(sentence)
    tags = []
    sentence = [word if word in word_index else '<unk>' for word in sentence]
    indices = [word_index[word] for word in sentence]
    y1 = np.argmax(init_st_vector * emis_matrix[indices[0], :])
    tags.append(y1)
    for i in range(1, T):
        yi = np.argmax(trans_matrix[tags[i - 1], :] * emis_matrix[indices[i], :])
        tags.append(yi)
    return tags


correct_tags = 0
total_tags = 0
for example in dev_data:
    sentence = example['sentence']
    true_tags = [state_index[label] for label in example['labels']]  # Convert labels to indices
    predicted_tags = greedyDecode(sentence)
    correct_tags += np.sum(np.equal(np.array(predicted_tags), np.array(true_tags)))
    total_tags += len(true_tags)
accuracy = correct_tags / total_tags
print(f"Accuracy on dev data: {accuracy * 100:.2f}%")

index_to_state = {i: s for s, i in state_index.items()}

results = []
for i, example in enumerate(test_data):
    sentence = example['sentence']
    tags = greedyDecode(sentence)
    tags = [index_to_state[tag] for tag in tags]  
    
    original_sentence = next((item['sentence'] for item in original_data if item['index'] == i), None)
    
    results.append({
        "index": i,
        "sentence": original_sentence,  
        "labels": tags
    })

with open('/Users/buckethoop/Downloads/544_HW2/verification/out/greedy.json', 'w') as file:
    json.dump(results, file, indent=4)