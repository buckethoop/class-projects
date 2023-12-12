import json
import math

with open('/Users/buckethoop/Downloads/544_HW2/verification/out/hmm.json', 'r') as file:
    hmm_data = json.load(file)
    
with open('modified_dev.json', 'r') as file:
    dev_data = json.load(file)

with open('modified_test.json', 'r') as file:
    test_data = json.load(file)

with open('/Users/buckethoop/Downloads/544_HW2/data/test.json', 'r') as file:
    original_data = json.load(file)

init_probs = hmm_data['initial']
trans_probs = hmm_data['transition']
emis_probs = hmm_data['emission']
states = list(init_probs.keys())

def checkEmission(sentence, emis_probs, states):
    checked_sentence = []
    for word in sentence:
        found = any(f"('{state}','{word}')" in emis_probs for state in states)
        if found:
            checked_sentence.append(word)
        else:
            checked_sentence.append('<unk>')  # Replace with a special unknown token
    return checked_sentence

def viterbiDecode(sentence, states, init_probs, trans_probs, emis_probs):
    T = len(sentence)
    K = len(states)
    
    T1 = [[-float('inf') for _ in range(T)] for _ in range(K)]
    T2 = [[0 for _ in range(T)] for _ in range(K)]
    
    for i, state in enumerate(states):
        emis_key = f"('{state}','{sentence[0]}')"
        T1[i][0] = math.log(max(init_probs[state], 1e-10)) + math.log(max(emis_probs.get(emis_key, 1e-10), 1e-10))
        T2[i][0] = 0
    
    for j in range(1, T):
        for i, state in enumerate(states):
            max_tra_prob = T1[0][j - 1] + math.log(max(trans_probs.get(f"('{states[0]}','{state}')", 1e-10), 1e-10))
            prev_st_select = 0
            for k, prev_state in enumerate(states[1:], start=1):
                tr_prob = T1[k][j - 1] + math.log(max(trans_probs.get(f"('{prev_state}','{state}')", 1e-10), 1e-10))
                if tr_prob > max_tra_prob:
                    max_tra_prob = tr_prob
                    prev_st_select = k
            max_prob = max_tra_prob + math.log(max(emis_probs.get(f"('{state}','{sentence[j]}')", 1e-10), 1e-10))
            T1[i][j] = max_prob
            T2[i][j] = prev_st_select
    
    best_path_prob = max(T1[i][-1] for i in range(K))
    best_lst_st_idx = -1
    for i in range(K):
        if T1[i][-1] == best_path_prob:
            best_lst_st_idx = i
            break
    best_lst_st = states[best_lst_st_idx]

    
    path = [best_lst_st]
    for j in range(T - 1, 0, -1):
        best_lst_st = states[T2[states.index(best_lst_st)][j]]
        path.insert(0, best_lst_st)
    
    return path

correct = 0
total = 0
for record in dev_data:
    sentence = checkEmission(record['sentence'], emis_probs, states)
    labels = record['labels']
    predicted_labels = viterbiDecode(sentence, states, init_probs, trans_probs, emis_probs)
    correct += sum(pred == tag for pred, tag in zip(predicted_labels, labels))
    total += len(labels)

accuracy = correct / total
print(f"Accuracy on dev data: {accuracy * 100:.2f}%")

results = []
for i, record in enumerate(test_data):
    mod_sentence = checkEmission(record['sentence'], emis_probs, states)
    predicted_labels = viterbiDecode(mod_sentence, states, init_probs, trans_probs, emis_probs)
    
    original_sentence = next((item['sentence'] for item in original_data if item['index'] == i), None)
    
    results.append({
        "index": i,
        "sentence": original_sentence,  # Storing original sentence
        "labels": predicted_labels
    })

with open('/Users/buckethoop/Downloads/544_HW2/verification/out/viterbi.json', 'w') as file:
    json.dump(results, file, indent=4)
