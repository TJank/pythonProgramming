# String

# Name
my_name = "Guarrionex Salivia"
#print(my_name)
#print(type(my_name))

# Indexing
#print(my_name[0])
#print(my_name[-1])
#print(len(my_name))


# Slicing
first_name = my_name[0:5]
#print(first_name)
last_name = my_name[-1:-10:-1]   # print last name in reverse
#print(last_name)

# a copy?
name_copy = my_name[:]
#print(name_copy)

# Immutable
# fi we try to reassign/change a value within a string we would try to do the following..
#my_name[5] = "-"    # receives an error
#print(my_name)

# print all the prefixes of my_name
#for i in range(1, len(my_name) + 1):
   # print(my_name[0:i])

# using an accumulator
prefix = ""
#for i in range(len(my_name)):
    #prefix += my_name[i]
    #print(prefix)

# print all the suffixes of my_name
#for i in range(1, len(my_name) + 1):
    #print(my_name[len(my_name)-i:])


# Function that calculates letter grade based on scores from 0-100

def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"


# build a function to test if x > y or x < y or x = y
def comparison(x, y):
    if x > y :
        return "{0} is greater than {1}".format(x,y)
    elif x < y:
        return "{0} is smaller than {1}".format(x, y)
    elif x == y:
        return "{0} is equal to {1}".format(x, y)
    else:
        print("Try again")

#print(comparison(5,2))

# Encryption: scrambling letters in a message

def scramble_encrypt(plain_text):
    encrypted1 = " " # accumulates characters in even indices
    encrypted2 = " " # odd indices

    flag = True

    for char in plain_text:
        if flag:
            encrypted1 += char
            flag = not flag
        else:
            encrypted2 += char
            flag = not flag

    return encrypted1 + encrypted2

print(20*"*" + "\n")
message = "Welcome to MNSU"
cipher_text = scramble_encrypt(message)
print(cipher_text)

def scramble_decrypt(cipher_text):
    # case where length of cipher_text is even
    slice1 = cipher_text[:len(cipher_text)//2]
    slice2 = cipher_text[len(cipher_text)//2:]
    middle = ""

    if not len(cipher_text) % 2 == 0:   #has odd length
        slice2 = cipher_text[len(cipher_text)//2 + 1:]
        middle = cipher_text[len(cipher_text)//2]

    plain_text = ""             # Came back to on 2-8-2018
    # slice1 and slice2 are of equal lengths
    for index in range(len(slice1)):
        plain_text += slice1[index] + slice2[index]

    plain_text += middle

    return plain_text

original_message = scramble_decrypt(cipher_text)
print(original_message)