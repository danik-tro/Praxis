import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
import sys



def retrive_definition(word):
    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word.title()]

    elif word.upper() in data:
        return data[word.upper()]

    elif len(get_close_matches(word, data.keys())) > 0:
        word_ = get_close_matches(word, data.keys())[0]
        action = input("Did you mean %s instead? [y or n] : " % word_)

        if action.lower() == 'y':
            return data[word_]
        elif action.lower() == 'n':
            return "The word doesn't exist, please double check it."

        return "We don't understand your entry. Apologies."
        
def main():
    
    word_user = input('->   Enter word. Or EXOUT, for exit from app: ')

    if word_user.lower() == 'exout':
        global check
        check = True
        return

    our_word = retrive_definition(word_user.lower())

    if type(our_word) == list:
        print('=>   ' + word_user.title() + '    <=\n')
        print(''.join(('    <-> {}\n'.format(i) for i in our_word)))
        print('=>   End.    <=\n')


if __name__ == "__main__":
    data = json.load(open("dictionary.json"))
    check = False
    while not check:
        main()
    print('\n=>     GoodBye :=)     <=')