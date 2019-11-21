import json
import difflib
from difflib import SequenceMatcher

data = json.load(open("dictionary.json"))

def retrive_definition(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    return "The word doesn't exist, please double check it."
        

word_user = input('Enter word: ')

print(retrive_definition(word_user.lower()))
