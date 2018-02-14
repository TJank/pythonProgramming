# 1.
sentence = "The quick brown fox jumped over the sleeping dog."
alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiouy"
consonants = "abcdfghjklmnpqrstvwxyz"
def missingLetters(sentence, alphabet):
    missing_ch = ""
    sentence = sentence.lower()
    for letter in alphabet:
        if not letter in sentence:
            missing_ch += letter
    return missing_ch

print(missingLetters(sentence, alphabet))

# 2.
# part 1
def numVowels(sentence, vowels):
    num_vowels = 0
    sentence = sentence.lower()
    for letter in sentence:
        if letter in vowels:
            num_vowels += 1
    return num_vowels

print(numVowels(sentence, vowels))

# part 2
def numConsonants(sentence, consonants):
    num_consonants = 0
    sentence = sentence.lower()
    for letter in sentence:
        if letter in consonants:
            num_consonants += 1
    return num_consonants

print(numConsonants(sentence, consonants))

# part 3
def allTogether(sentence, vowels, consonants):
    return numVowels(sentence, vowels) + numConsonants(sentence, consonants)

print(allTogether(sentence, vowels, consonants))

# 3.
word = "word"*3
