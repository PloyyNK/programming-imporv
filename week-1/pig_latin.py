"""Pig Latin is a language game in which English words are altered, by move the fist
consonant to the back and add ay. In case the word start with vowel, we simply add
the word way to the back."""
import sys

# Steps
#     : Get user sentence
#     : Split the sentence into list of words
#     : Check if word have vowel
#     : Print the translated sentence in red


sentence = input("Enter your sentence: ").lower()
words = sentence.split()
vowels = ['a', 'e', 'i', 'o', 'u']

for i, word in enumerate(words):
    if word[0] in vowels:
        words[i] = word + 'way'
    else:
        words[i] = word[1:] + word[0] + 'ay'

translated_sentence = ' '.join(words)
print("Pig Latin: ", end="")
print(translated_sentence, file=sys.stderr)
