# Steps
#     : Get user sentence
#     : Split the sentence into list of words
#     : Check if word have vowel
#     : Print the translated sentence


sentence = input("Enter your sentence: ").lower()
words = sentence.split()
vowels = ['a', 'e', 'i', 'o', 'u']

for i, word in enumerate(words):
    if word[0] in vowels:
        words[i] = word + 'way'
    else:
        words[i] = word[1:] + word[0] + 'ay'

translated_sentence = ' '.join(words)
print(f"Pig Latin: {translated_sentence}")
