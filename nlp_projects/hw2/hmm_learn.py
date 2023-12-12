import json
import numpy as np
from collections import defaultdict

with open('/Users/buckethoop/Downloads/544_HW2/modified_train.json', 'r') as file:
    train_data = json.load(file)

pseudo_words = {
    "twoDigitNum", 
    "fourDigitNum", 
    "initCap",
    "containsDigitAndSlash", 
    "containsDigitAndPeriod",
    "abbreviation", 
    "<unk>"
}

states = set()
observations = set(pseudo_words)
for sequence in train_data:
    states.update(sequence["labels"])
    observations.update(sequence["sentence"])

state_idx = {state: idx for idx, state in enumerate(states)}
obs_idx = {obs: idx for idx, obs in enumerate(observations)}

state_num = len(states)
obs_num = len(observations)

init_count = np.zeros(state_num)
trans_count = np.zeros((state_num, state_num))
emis_count = np.zeros((state_num, obs_num))

for sequence in train_data:
    labels = sequence["labels"]
    sentence = sequence["sentence"]
    
    init_count[state_idx[labels[0]]] += 1
    
    for i in range(len(labels)):
        curr_state_idx = state_idx[labels[i]]
        curr_obs_idx = obs_idx[sentence[i]]
        emis_count[curr_state_idx, curr_obs_idx] += 1
        
        if i > 0:
            prev_state_idx = state_idx[labels[i - 1]]
            trans_count[prev_state_idx, curr_state_idx] += 1

alpha = 1
emis_count += alpha
row_sum = emis_count.sum(axis=1, keepdims=True)
emission_probs = emis_count / row_sum

init_probs = init_count / sum(init_count)
trans_probs = trans_count / trans_count.sum(axis=1, keepdims=True)

init_dict = {s: init_probs[state_idx[s]] for s in states}
trans_dict = {f"('{s}','{s_prime}')": trans_probs[state_idx[s], state_idx[s_prime]] 
                   for s in states for s_prime in states}
emis_dict = {f"('{s}','{x}')": emission_probs[state_idx[s], obs_idx[x]] for s in states for x in observations}

hmm_model = {
    "initial": init_dict,
    "transition": trans_dict,
    "emission": emis_dict
}

print("Number of Transition Parameters:", state_num * state_num)
print("Number of Emission Parameters:", state_num * obs_num)

with open('/Users/buckethoop/Downloads/544_HW2/verification/out/hmm.json', 'w') as file:
    json.dump(hmm_model, file, indent=4)
