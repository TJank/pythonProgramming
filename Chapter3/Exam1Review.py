# Exam 1 Study Guide
import random

# Removing Spaces from a string
def remove_spaces(message, removeString):
    new_string = " "
    for ch in message:
        if ch not in removeString:
            new_string = new_string + ch
    return new_string

message = "The quick brown fox"
#print(remove_spaces(message, " "))

# Generating random keyword
alphabet = "abcdefghijklmnopqrstuvwxyz"

def keyWord(wordLength, alphabet):
    key = ""

    while len(key) < wordLength:
        idx = random.randint(0, len(alphabet) - 1)

        if not alphabet[idx] in key:
            key += alphabet[idx]

    return key

#print(keyWord(5, alphabet))

# List of numbers - ascending order
list = [1,5,7,9,2,3]
#print(sorted(list))

def sortList(listOfNumbers):
    list = sorted(listOfNumbers)
    return list

print(sortList(list))

def decimal_to_binary(decimalNum):
    if decimalNum == 0:
        return "00000000"
    binary = ""
    while decimalNum > 0:
        binary = str(decimalNum % 2) + binary
        print(binary)
        decimalNum = decimalNum//2

    if len(binary) % 8 != 0:
        print(len(binary))
    return binary

#decimal_to_binary(48)

def DecToBin(num):
    binaryNum = "\0"
    while(num>0):
        temp = num % 2
        binaryNum = str(temp) + binaryNum
        num = int(num/2)

    apz = len(binaryNum) % 8
    while(apz>1):
        binaryNum = "0" + binaryNum
        apz =apz - 1

    return binaryNum

print(DecToBin(48))

# 20 sided die
def twenty_sided_die(numrolls):

    for i in range(0,numrolls+1):
        if i < numrolls+1:
            sideUp = random.randrange(1, 21)
            if sideUp == 1:
                print("You rolled a 1.")
            elif sideUp == 2:
                print("Your rolled a 2.")
            elif sideUp == 3:
                print("Your rolled a 3.")
            elif sideUp == 4:
                print("Your rolled a 4.")
            elif sideUp == 5:
                print("Your rolled a 5.")
            elif sideUp == 6:
                print("Your rolled a 6.")

#twenty_sided_die(6)


