# Chapter 3 homework
# Question 1.
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

# Question 2.
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

# Question 3.
word = "word" * 3
first = word[:3]
i = word[3:4]
middle = word[4:8]
j = word[8:9]
last = word[9:]
print(first + j + middle + i + last)

# Question 4
num = 8128

def perfectNum(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum

print(perfectNum(num))

# 5
telephoneUpper = {('A', 'B', 'C'): 2, ('D', 'E', 'F'): 3, ('G', 'H', 'I'): 4,
                      ('J', 'K', 'L'): 5, ('M', 'N', 'O'): 6, ('P', 'Q', 'R', 'S'): 7,
                      ('T', 'U', 'V'): 8, ('W', 'X', 'Y', 'Z'): 9}
telephoneLower = {('a', 'b', 'c'): 2, ('d', 'e', 'f'): 3, ('g', 'h', 'i'): 4,
                      ('j', 'k', 'l'): 5, ('m', 'n', 'o'): 6, ('p', 'q', 'r', 's'): 7,
                      ('t', 'u', 'v'): 8, ('w', 'x', 'y', 'z'): 9}

#def getNumber(phoneNumber):

# Question 6
def passwrdCheck(password):
    password = password.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz 1234567890"
    digits = "0123456789"
    num_digits = 0

    # Checks for at least 8 characters
    if len(password) < 8:
        print("Your password is invalid, must contain 8 characters.")

    # Checks for at least 2 numbers
    for ch in password:
        if ch in digits:
            num_digits += 1

    if num_digits < 2:
        print("Your password is invalid, must contain at least 2 numbers.")

    # Checks for letters or numbers in password
    for ch in password:
        if not ch in alphabet:
            print("Your password is invalid, must contain only numbers and letters.")
    else:
        print("Your password is valid.")

passwrdCheck("password")







