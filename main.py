import re
import sys
import os
import json
from datacleaner import cleaner

def convertToJSON():
    with open('data/input.txt', 'r') as f:
        text = f.read()
    with open('data/database.json', 'w') as db:
        json.dump(cleaner.parse(text), db)

def search(word):
    word = word.upper()
    with open('data/database.json', 'r') as db:
        dictionary = json.load(db)
    try:
        return dictionary[word]
    except:
        return 'Word doesn\'t exist in dictionary'

def view(word):
    result = search(word)
    if type(result) is list:
        print('------------------------')
        print(word.upper())
        [print('\t*',i) for i in result]
    else:
        print(result)

def complex_search():
    word = []
    length = input('length of the word:')
    print('If you know some of the letters in the word, then you can put them here')
    print('Else, just press enter')
    for i in range(int(length)):
        while True:
            letter = input('Letter ' + str(i+1)+':')
            if len(letter) == 0:
                word.append('_')
                break
            elif re.fullmatch(r'[a-zA-Z]', letter):
                if len(letter) == 1:
                    word.append(letter.upper())
                    break
                else:
                    print('you can not type more than a letter here')
            else:
                print('you have to put in a valid letter')

    print('Your letter looks like this')
    print(' '.join(word))
    input('Click enter to continue')
    regex = ''
    for letter in word:
        if letter == '_':
            regex += '[a-zA-Z]'
        else:
            regex += letter
    with open('data/database.json', 'r') as db:
        dictionary = json.load(db)
    searchwords = []
    for i in dictionary:
        if re.fullmatch(regex,i):
            searchwords.append(i)
    for i in searchwords:
        view(i)
    if input('Click enter to start over, "q" to quit: ') == 'q':
        sys.exit()
    os.system('clear')  # on linux / os x

while True:
    print('Pick an option')
    print('1.\t Search the exact word:')
    print('2.\t Search part of the word:')
    choice = input('number here: ')
    if choice == '1':
        view(input('Search: '))
        if input('Click enter to start over, "q" to quit: ') == 'q':
            sys.exit()
        os.system('clear')  # on linux / os x
    elif choice == '2':
        complex_search()
