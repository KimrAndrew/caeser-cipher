import nltk

nltk.download('words', quiet = True)
nltk.download('names', quiet = True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()
import re

def shift_char(char,shift):
    char_code = ord(char)
    if ord('A') <= char_code <= ord('Z'):
        shifted_code = char_code + shift
        if shifted_code > ord('Z'):
            wrap = shifted_code % ord('Z')
            shifted_code = ord('A') + wrap
        if shifted_code < ord('A'):
            wrap = 1 + (ord('A') % shifted_code) * -1
            shifted_code = ord('Z') + wrap
        shifted_char = chr(shifted_code)
        return shifted_char
    elif ord('a') <= char_code <= ord('z'):
        shifted_code = char_code + shift
        if shifted_code > ord('z'):
            wrap = shifted_code % ord('z')
            shifted_code = ord('a') + wrap
        if shifted_code < ord('a'):
            wrap = 1 + (ord('a') % shifted_code) * -1
            shifted_code = ord('z') + wrap
        shifted_char = chr(shifted_code)
        return shifted_char
    else:
        return char


def encrypt(plain,shift):
    encrypted = ''
    for char in plain:
        encrypted += shift_char(char,shift)
    return encrypted

def decrypt(encrypted,shift):
    return encrypt(encrypted, -shift)

def crack(encrypted):
    cracked = []
    for shift in range(26):
        cracked.append(decrypt(encrypted,shift))
    return cracked

def get_valid_words(candidate_phrase):
    words = []
    for candidate_word in candidate_phrase:
        candidate_word = re.sub(r'[^a-zA-Z]+')
        if candidate_word.lower() in word_list or candidate_word in name_list:
            words.append(candidate_word)
    return words

def get_phrase_validity_percentage(candidate_phrase):
    denominator = len(candidate_phrase.split())
    nummerator = len(get_valid_words(candidate_phrase))
    percentage = int(nummerator / denominator) * 100
    return percentage

def get_most_valid_phrase(candidate_phrases):
    candidate_percentages = {}
    for candidate_phrase in candidate_phrases:
        candidate_percentages[candidate_phrase] = get_phrase_validity_percentage(candidate_phrase)
    most_valid = ''
    for candidate_phrase in candidate_percentages:
        if candidate_percentages.get(candidate_phrase) > candidate_percentages.get(most_valid):
            most_valid = candidate_phrase
    return max
        
            


if __name__ == '__main__':
    print(shift_char('H',26))
    #print(shift_char('H',25))
    #print(shift_char('H',24))
    print(shift_char('H',23))
    #print(shift_char('h',26))
    #print(shift_char('h',25))
    #print(shift_char('h',24))
    #print(shift_char('h',23))
    #print(encrypt('Hello_World!!',3))
    #print(decrypt('KHOOR_ZRUOG!!',3))
    #print(crack('KHOOR_ZRUOG!!'))
    print(crack('HELLO_WORLD!!!'))
    print(crack('hello_world!!!'))

