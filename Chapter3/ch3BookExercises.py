# PG 89
name = "Tyler Jonathan Jankowski"
firstname = name[0:5]
lastname = name[15:len(name) +1]
print(lastname + ", " + firstname)
print(len(firstname))

s = "s"
p = "p"

mississippi = "mi" + s + s + "i" + s + s + "i" + p + p + "i"
#print(mississippi)

name2 = "Roy G Biv"
#for i in range(len(name2) + 1):
    #print(name2[0:i])

# PG 91
mis = "mississippi"
#print(mis.count("s"))
#print(mis.replace("iss", "ox"))
#print(mis.index("p"))
p = "python"
p = p.upper()
#print(p.center(20))

# Listing 3.1 PG 93
def letterToIndex(ch):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    idx = alphabet.find(ch)
    if idx < 0:
        print("error: letter not in the alphabet", ch)
    return idx

def indexToLetter(idx):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    if idx > 25:
        print("error: ", idx, " is too large.")
        letter = ""
    elif idx < 0:
        print("error: ", idx, " is less than 0.")
        letter = ""
    else:
        letter = alphabet[idx]
    return letter

#print(letterToIndex("t"))
#print(indexToLetter(19))

# PG 93 Exercises
#print(ord('a'))
#print(ord('A'))
def characterToIntValue(ch):
    print(ord(ch))

#characterToIntValue('A')

# Listing 3.2 PG 95
def scramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText

pText = "own noun brown cow"




# Continued pg 98
def scramble2Decrypt(cipherText):
    halfLength = len(cipherText) // 2
    oddChars = cipherText[:halfLength]
    evenChars = cipherText[halfLength:]
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]

    return plainText

cipherTEXT = scramble2Encrypt(pText)

plainText = scramble2Decrypt(cipherTEXT)

print(cipherTEXT)
print(plainText)

# Listing 3.5 PG 102 encryption using a substitution cipher
def substitionEncrypt(plainText, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    plainText = plainText.lower()
    cipherText = ""
    for ch in plainText:
        idx = alphabet.find(ch)
        cipherText = cipherText + key[idx]
    return cipherText

testkey1 = "zyxwvutsrqponmlkjihgfedcba "
testkey2 = "ouwckbjmpzyexavrltsfgdqihn "

#ipher_text = substitionEncrypt("the quick brown fox", testkey1)
#print(cipher_text)
#cipher_text = substitionEncrypt("the quick brown fox", testkey2)
#print(cipher_text)

def substitutionDecrypt(cipher_text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    plain_text = ""
    for ch in cipher_text:
        idx = key.find(ch)
        plain_text = plain_text + alphabet[idx]
    return plain_text

cipher_text = substitionEncrypt("the quick brown fox", testkey1)
print(cipher_text)
plain_text = substitutionDecrypt(cipher_text, testkey1)
print(plain_text)