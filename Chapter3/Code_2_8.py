# Substitution (Caesar Cipher)
import string

alphabet = string.ascii_lowercase + " ,?."

my_key = "defghijklmnopqrstuvwxyzabc,?. "

def substitution_encryption(plain_text, alphabet, key):
    plain_Text = plain_text.lower()
    cipher_text = ""
    for ch in plain_Text:
        idx = alphabet.find(ch)
        cipher_text += key[idx]

    return cipher_text

#message = "Hello World"
#cipher_text = substitution_encryption(message, alphabet, my_key)
#print(cipher_text)

message = "Is anybody out there? If there is, please respond."
cipher_text = substitution_encryption(message, alphabet, my_key)
print(cipher_text)

def substitution_decryption(cipher_text, alphabet, key):
    cipherText = cipher_text.lower()
    plain_text = ""
    for ch in cipherText:
        idx = key.find(ch)
        plain_text += alphabet[idx]

    return plain_text

original_message = substitution_decryption(cipher_text, alphabet, my_key)
print(original_message)



# Key Generator
#idea: randomize alphabet letters
import random

def key_gen(alphabet= string.ascii_lowercase + " "):
    key = ""

    # run as many times as the length of the alphabet
    while len(key) < len(alphabet):
        # select a random index
        # indices can be selected using randint(a,b)
        idx = random.randint(0, len(alphabet) - 1)

        if not alphabet[idx] in key:
            key += alphabet[idx]

    return key

key = key_gen()
print(key)
