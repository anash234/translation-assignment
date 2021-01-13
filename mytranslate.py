#!/usr/bin/python3
'''
This program is from p. 81 Figure 5.9 "Translating text (badly)" of 
our Gutag textbook.
You can use it as a starter program for assignment 2.

The output from the program is:
--------------------------------------
Input: I drink good red wine, and eat bread.
Output: Je bois "good" rouge vin, et mange pain..
--------------------------------------
Input: Je bois du vin rouge.
Output: I drink of wine red..
--------------------------------------
'''


def reverseDictionary(dictionary):          # This function reverses a dictionary
    reverse = {}                            # Creates an empty dictionary to store the reversal in
    for word in dictionary.keys():          # Loops over each key in the input dictionary
        reverse[dictionary[word]] = word    # Creates an entry in reverse where the key and value are switched
    return reverse                          # Returns the reversed dictionary


def combineDictionaries(AtoB, AtoC):        # Uses dictionaries AtoB and AtoC to create BtoC
    BtoC = {}                               # Creates empty dictionary to store BtoC
    for word in AtoB.keys():                # For each key in AtoB, creates BtoC entry using that key's
        BtoC[AtoB[word]] = AtoC[word]       # values in AtoB and AtoC respectively
    return BtoC                             # Returns BtoC


EtoF = {'bread': 'pain', 'wine': 'vin', 'with': 'avec', 'I': 'je', 'eat': 'mange', 'drink': 'bois',
        'John': 'Jean', 'friends': 'amis', 'and': 'et', 'some': 'du', 'red': 'rouge', 'good': 'bon',
        'the': 'le', 'one': 'un', 'two': 'deux', 'three': 'trois', 'four': 'quatre', 'five': 'cinq',
        'six': 'six', 'seven': 'sept', 'eight': 'huit', 'nine': 'neuf', 'ten': 'dix', 'you': 'tu',
        'he': 'il', 'she': 'elle', 'my': 'mon', 'your': 'ton', 'his': 'son', 'her': 'sa', 'play': 'joue',
        'cat': 'chat', 'dog': 'chien', 'house': 'maison', 'cook': 'cuisine', 'meal': 'repas', 'am': 'suis',
        'are': 'es', 'is': 'est', 'happy': 'content', 'sad': 'triste', 'nice': 'gentil', 'great': 'sympa',
        'visit': 'visite', 'see': 'vois', 'talk': 'parle', 'say': 'dis', 'sing': 'chante', 'walk': 'marche',
        'laugh': 'ris'}
# Added: good, the, one, two, three, four, five, six, seven, eight, nine, ten, you, he, she
# my, your, his, her, play, cat, dog, house, cook, meal, am, are, is, happy, sad, nice, great
# visit, see, talk, say, sing, walk, laugh

EtoR = {'bread': 'khleb', 'wine': 'vino', 'with': "s'", 'I': 'ya', 'eat': 'yem', 'drink': "p'yu",
        'John': 'Jon', 'friends': "druz'ya", 'and': 'i', 'some': 'nekotoryye', 'red': 'krasnyy', 'good': 'khoroshiy',
        'the': 'v', 'one': 'odin', 'two': 'dva', 'three': 'tri', 'four': 'chetyre', 'five': "pyat'",
        'six': "shest'", 'seven': "sem'", 'eight': "vosem'", 'nine': "devyat'", 'ten': "desyat'", 'you': 'vy',
        'he': 'on', 'she': 'ona', 'my': 'moy', 'your': 'vash', 'his': 'yego', 'her': 'yeye', 'play': "igrat'",
        'cat': 'koshka', 'dog': 'sobaka', 'house': 'dom', 'cook': 'gotovlyu', 'meal': 'yeda', 'am': "yest'",
        'are': 'byl', 'is': "byt'", 'happy': 'schastlivyy', 'sad': "pechal'nyy", 'nice': 'otlichno',
        'great': "bol'shoy", 'visit': 'poseshchayu', 'see': 'ponimayu', 'talk': 'govoryu', 'say': "govorish'",
        'sing': 'poyu', 'walk': 'idu', 'laugh': "smeyus'"}

FtoE = reverseDictionary(EtoF)

RtoE = reverseDictionary(EtoR)

FtoR = combineDictionaries(EtoF, EtoR)

RtoF = combineDictionaries(EtoR, EtoF)

dicts = {'English to French': EtoF, 'French to English': FtoE, 'English to Russian': EtoR,
         'Russian to English': RtoE, 'French to Russian': FtoR, 'Russian to French': RtoF}


def translateWord(word, dictionary):   # This function tries to translate any given word
    if word in dictionary.keys():       # Checks if the word is in the dictionary
        return dictionary[word]         # If it is, returns the translation
    elif word != '':                    # Checks if the word is an empty string
        return '"' + word + '"'         # If it is neither in the dictionary nor empty, returns it in quotes
    return word


def capitalize(phrase):     # Capitalizes the first letter in each sentence of a phrase
    capitalized = phrase    # Creates a copy of the phrase which will be capitalized
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'    # Identifies letters
    if phrase[0] in letters and phrase[0].upper() != phrase[0]:         # Checks if the first character is a lowercase
        capitalized = phrase[0].upper() + phrase[1:]                    # letter; if so, capitalizes it
    index = 0                   # Counts what index of the phrase the following loop has reached
    for character in phrase:    # Loops over each character in the phrase looking for periods
        if index < len(phrase) - 2:                         # Checks if the index is too close to the end of the phrase
            if character == '.' and phrase[index + 2] in letters:   # Identifies letters two characters after a period
                capitalized = capitalized[0:index + 2] + capitalized[index + 2].upper() + capitalized[index + 3:]
            index += 1  # Last line capitalizes the identified letter and adds to new phrase; this one updates the index
    return capitalized  # Returns the correctly capitalized phrase


def translate(phrase, dicts, direction):        # Translates a phrase, using dictionaries and direction of translation
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'"    # Identifies letters (to use to identify words)
    dictionary = dicts[direction]   # Chooses which dictionary to use in dicts based on direction of translation
    translation = ''
    word = ''
    for character in phrase:            # This runs through each character in the phrase
        if character in letters:        # Checking if it is a letter
            word = word + character     # And identifying groups of letters separated by non-letters as words
        else:                           # Once a space or punctuation is reached, stops building the word
            if word == 'I' or word == 'John' or word == 'Jean':             # Checks if the word needs a capital letter
                translation += translateWord(word, dictionary) + character      # Adds the translated word and
                word = ''   # Resets the 'word' variable                          its punctuation to translation
            else:                                # If the word does not need a capital letter, changes to lowercase
                translation += translateWord(word.lower(), dictionary) + character  # Adds the translated word and
                word = ''                       # Resets the 'word' variable          its punctuation to translation
    translation = capitalize(translation)       # Correctly capitalizes the translated phrase
    return translation      # Returns the translated phrase


sentence = 'I drink good red wine and eat bread.'
translated = translate(sentence, dicts, 'English to French')
print('--------------------------------------')
print('Input:', sentence)
print('Output:', translated)
print('--------------------------------------')
sentence = 'Je bois du vin rouge.'
translated = translate(sentence, dicts, 'French to English')
print('Input:', sentence)
print('Output:', translated)
print('--------------------------------------')
sentence = 'I drink good red wine and eat bread.'
translated = translate(sentence, dicts, 'English to Russian')
print('--------------------------------------')
print('Input:', sentence)
print('Output:', translated)
print('--------------------------------------')
sentence = "Ya p'yu khoroshiy krasnyy vino i yem khleb."
translated = translate(sentence, dicts, 'Russian to English')
print('Input:', sentence)
print('Output:', translated)
print('--------------------------------------')
sentence = "Ya p'yu khoroshiy krasnyy vino i yem khleb."
translated = translate(sentence, dicts, 'Russian to French')
print('--------------------------------------')
print('Input:', sentence)
print('Output:', translated)
print('--------------------------------------')
sentence = 'Je bois du vin rouge.'
translated = translate(sentence, dicts, 'French to Russian')
print('Input:', sentence)
print('Output:', translated)
print('--------------------------------------')

'''Improvements:
1. Added comments, minor tweaks to code (e.g. letters in translate function)
2. Fixed double period glitch by removing the second-last line in translate function
3. Wrote reverseDictionary function, replaced FtoE with reverseDictionary(EtoF)
4. Added ability to translate words with uppercase letters
5. Wrote capitalize function to correctly capitalize sentences, called in translate function
6. Dictionary improvements: changed 'Je' to 'je', changed translation of 'du' to 'some', added 39 words (total 50)
7. Added English to Russian dictionary
8. Wrote combineDictionaries to make FtoR and RtoF out of EtoF and EtoR dictionaries
'''
