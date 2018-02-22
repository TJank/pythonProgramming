# Vignere Cipher
# Divide and Conquer
# 1. Fix key to be the same length as a message
# 2. Make sure key is upper case and message is lower case
# 3. Create a Vignere Square that can be used to encrypt the message
#   3.1 Vignere Square depends on an alphabet
# 4. Encode by mapping a pair (X, Y) -> Z where X is a letter from
# the key, Y is a letter from the message and Z can be found in the
# Vignere Square

import string


def create_keyword(keyword, n):
    """
    Function to create an appropriate keyword to be used in a Vignere Cipher
    encryption system
    :param keyword: any string
    :param n: length of the message to be encrypted
    :return: new keyword with length n
    """

    new_keyword = ""
    idx = 0

    if len(keyword) < n:    # new_keyword need to grow up to size n
        for i in range(n):
            if idx >= len(keyword):
                idx = 0

            new_keyword += keyword[idx]
            idx += 1

        return new_keyword

    elif len(keyword) > n:
        return keyword[:n]

    else:
        return keyword


message = "Barca Sucks"
key = "happybirthday"
#key = "lime"

new_keyword = create_keyword(key, len(message))
print(new_keyword)


def vignere_square(alphabet=string.ascii_lowercase):
    vs = dict()

    # Copy to shift
    alphabet_to_shift = alphabet.lower()

    # Copy for the Rows (upper case)
    upper_case = alphabet.upper()

    # Copy for the Columns (lower case)
    lower_case = alphabet.lower()


    for upper in upper_case:
        for lower in lower_case:
            idx = lower_case.index(lower)
            vs[upper, lower] = alphabet_to_shift[idx]

        alphabet_to_shift = alphabet_to_shift[1:] + alphabet_to_shift[0]

    return vs

#print(vignere_square())
#print(len(vignere_square()))

vs = vignere_square(string.ascii_lowercase + " ")
print(vs)


def vignere_encryption(message, key, alphabet):
    # Create a keyword
    new_keyword = create_keyword(key, len(message))

    # Create a Vignere Square
    vs = vignere_square(alphabet)

    # To use the Vignere Square the message must be in lower case
    # and the new_keyword must be in upper case
    new_keyword = new_keyword.upper()
    plain_text = message.lower()

    cipher_text = ""
    for i in range(len(plain_text)):
        cipher_text += vs[new_keyword[i], plain_text[i]]

    return cipher_text


cipher_text = vignere_encryption(message, key, string.ascii_lowercase + " ")
print(cipher_text)


# Practice: How do you reverse the encryption process?

# Practice: Encode the declaration of independence using Vignere Cipher.
declaration = "When in the Course of human events \
it becomes necessary for one people to dissolve \
the political bands which have connected them with \
another and to assume among the powers of the earth, \
the separate and equal station to which the Laws of Nature \
and of Nature's God entitle them, a decent respect to the \
opinions of mankind requires that they should declare the \
causes which impel them to the separation."

alphabet = ".', " + string.ascii_lowercase

print("-" * 20)
cipher_text = vignere_encryption(declaration, "freedom", alphabet)
print(cipher_text)

print(len(declaration), len(cipher_text))

# How do you reverse the encryption process?

# HINT: How do you extract a key from a dictionary with a given value?
def undoVig(keyLetter, ctLetter):
    character = ""
    character = character + vs[keyLetter]

def decryptVignere(cipher_text, keyword):
    plain_text = ""
    for i in range(len(cipher_text)):
        ch = vs[cipher_text[i] : keyword[i]]
        plain_text = plain_text + ch

print(decryptVignere(cipher_text, "freedom"))
