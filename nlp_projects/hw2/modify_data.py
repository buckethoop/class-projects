import json
import re
from collections import defaultdict


with open('/Users/buckethoop/Downloads/544_HW2/data/test.json', 'r') as file:
    data = json.load(file)

def wordToPseudo(word):
    if re.match(r"^\d{2}$", word):
        return "twoDigitNum"
    elif re.match(r"^\d{4}$", word):
        return "fourDigitNum"    
    elif re.match(r"^[A-Z]\.$", word):
        return "initCap"  
    elif re.match(r"^\d+/\d+(/\d+)*$", word):
        return "containsDigitAndSlash"
    elif re.match(r"^\d+\.\d+$", word): 
        return "containsDigitAndPeriod"  
    elif re.match(r"^[A-Z]{1,}\.$", word):
        return "abbreviation"    
    else:
        return word

word_freq = defaultdict(int)
for sequence in data:
    sentence = sequence["sentence"]
    for word in sentence:
        mod_word = wordToPseudo(word)
        word_freq[mod_word] += 1

threshold = 2

for sequence in data:
    sentence = sequence["sentence"]
    mod_sentence = [wordToPseudo(word) if word_freq[wordToPseudo(word)] >= threshold else '<unk>' for word in sentence]
    sequence["sentence"] = mod_sentence

with open('modified_test.json', 'w') as file:
    json.dump(data, file, indent=4)
