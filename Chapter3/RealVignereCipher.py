import string

# COMPLETE VIGNERE CIPHER CODE
# ENCRYPT AND DECRYPT PART OF DECLARATION OF INDEPENDENCE


# CREATION OF VIGNERE SQUARE
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


# CREATION OF NEW KEYWORD BASED ON KEYWORD AND LENGTH OF MESSAGE
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


# ENCRYPT MESSAGE WITH VIGNERE SQUARE
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



# RETRIVAL OF CHARACTERS TO MAKE DE-CODED MESSAGE AS PLAIN TEXT
def getMessage(key, en, vs):
    for j in vs.values():

        for i in vs.keys():
            if i[0]==key and j == en:
                if vs[i]==j:
                    return i[1]
                print(i)
                #return i[1]


# DECRYPTION OF VIGNERE CIPHER

def vignere_decryption(message, key, alphabet):
    # Create a keyword
    new_keyword = create_keyword(key, len(message))

    # Create a Vignere Square
    vs = vignere_square(alphabet)

    # To use the Vignere Square the message must be in lower case
    # and the new_keyword must be in upper case
    new_keyword = new_keyword.upper()
    plain_text = message.lower()

    decipher_text = ""
    for i in range(len(plain_text)):
        decipher_text += getMessage(new_keyword[i], plain_text[i], vs)



    return decipher_text


declaration = "When in the Course of human events \
it becomes necessary for one people to dissolve \
the political bands which have connected them with \
another and to assume among the powers of the earth, \
the separate and equal station to which the Laws of Nature \
and of Nature's God entitle them, a decent respect to the \
opinions of mankind requires that they should declare the \
causes which impel them to the separation."

alphabet =  string.ascii_lowercase+".', "
key = "freedom"

# CALLING VIGNERE SQUARE ENCRYPTION
cipher_text = vignere_encryption(declaration, "freedom", alphabet)
#print(cipher_text)

# VIGNERE SQUARE DECRYPTION
plain_text = vignere_decryption(cipher_text,"freedom",alphabet)
#print(plain_text)


