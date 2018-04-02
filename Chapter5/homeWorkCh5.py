# Code for chapter 5 homework
import random
# Problem 1.
def scramble(inputstring):
    # split each letter into list

    wordlist = list(inputstring)

    # get random integers for rotating

    i = random.randint(1, len(inputstring) - 2)

    j = random.randint(1, len(inputstring) - 2)

    # rotate the letter

    wordlist[i], wordlist[j] = wordlist[j], wordlist[i]

    # convert the list into string

    Result_str = ''.join(wordlist)

    # return the resultant string

    return Result_str

#print(scramble("trampoline"))


def scramblePara(longstring):
    scrambled_para = ""
    word = []

    for i in range(len(longstring)):
        #print(i, longstring[i])
        if longstring[i] == " ":
            scramble_word = ''.join(word)
            new_word = scramble(scramble_word)
            scrambled_para = scrambled_para + " " + new_word

        else:
            word.append(longstring[i])

    return scrambled_para


inputstring = 'This is my input string going to scramble.'
#print(scramblePara(inputstring))


# Problem 2.
def allActors(movie_title1, movie_title2):
    readfile = open("movies.txt", "r")
    actor_listA = []
    actor_listB = []
    readfile.readline()

    for aline in readfile:
        new_line = aline.split(',')
        if new_line[0] == movie_title1:
            #print("NewLine",new_line)
            actors = new_line[3:]
            actor_listA = actor_listA + actors
        elif new_line[0] == movie_title2:
            #print("newline", new_line)
            actors = new_line[3:]
            actor_listB = actor_listB + actors


    readfile.close()
    return actor_listA, actor_listB

movie1 = "16th December"
movie2 = "Cheenti Cheenti Bang Bang"
#print(allActors(movie1, movie2))

# Part B
def commonActors(movie_title1, movie_title2):
    readfile = open("movies.txt", "r")
    actor_listA = []
    actor_listB = []
    similar_actors = []
    readfile.readline()

    for aline in readfile:
        new_line = aline.split(',')

        if new_line[0] == movie_title1:
            #print(new_line)
            actor_listA = actor_listA + new_line[3:]
            #print("List A", actor_listA)
            #print("-"*20)

        if new_line[0] == movie_title2:
            #print(new_line)
            actor_listB = actor_listB + new_line[3:]
            #print("List B", actor_listB)

    for actor in actor_listA:
        if actor in actor_listB:
            #print(actor)
            similar_actors.append(actor)

    readfile.close()

    return similar_actors



movie_one = 'Fox'
movie_two = 'Familywala'
#print(commonActors(movie_one, movie_two))

# Part C
def unCommonActors(movie_title1, movie_title2):
    readfile = open("movies.txt", "r")
    actor_listA = []
    actor_listB = []
    actors = []
    readfile.readline()

    for aline in readfile:
        new_line = aline.split(',')

        if new_line[0] == movie_title1:
            #print(new_line)
            actor_listA = actor_listA + new_line[3:]
            #print("List A", actor_listA)
            #print("-"*20)

        if new_line[0] == movie_title2:
            #print(new_line)
            actor_listB = actor_listB + new_line[3:]
            #print("List B", actor_listB)

    for actr in actor_listA:
        if not actr in actors:
            actors.append(actr)

    for actr in actor_listB:
        if not actr in actors:
            actors.append(actr)

    readfile.close()

    return actors


#print(unCommonActors(movie_one, movie_two))



# Problem 3.
# find <a in a string
tail_test = '/future-students/apply/">Apply</a></li>'
def retrieveText(tail):
    text = ""

    for i in range(len(tail)):

        if tail[i] == ">" and tail[i-1] == '"':
            idx_of_beginning = tail[i+1]
            if tail[i] == "<" and tail[i+1] == "/":
                idx_of_end = tail[i]
                text = tail[idx_of_beginning: idx_of_end]

    return text

print(retrieveText(tail_test))

def findATags():
    readfile = open("looking_for_a_tags.txt", "r")
    a_tagList = []



    readfile.readline()
    for aline in readfile:
        for i in range(len(aline)):
            if aline[i] == "<" and aline[i + 1] == "a":
                tail = aline[i + 1:]
                #print(tail)
                if "href=''" in tail:
                    idx = tail.index("href")
                    idx += 6
                    tail2 = tail[idx:]
                    href = tail2[: tail2.index("'")]
                    #print("HREF FROM IF", href)
                elif "href=\"" in tail:
                    idx = tail.index("href")
                    idx += 6
                    tail2 = tail[idx:]
                    text = retrieveText(tail2)
                    print(tail2)
                    href = tail2[: tail2.index('"')]
                    print("HREF FROM ELIF", href)
                    a_tagList.append(href)

    return a_tagList



#print(findATags())


# Problem 4.
def averageSteps():
    months = ["January", "February", "March","April","May","June","July","August","September","October","November","December"]
    month_avg = []
    readfile = open("steps.txt", "r")

    januaryAvg = 0
    februaryAvg = 0
    marchAvg = 0
    aprilAvg = 0
    mayAvg = 0
    juneAvg = 0
    julyAvg = 0
    augustAvg = 0
    septemberAvg = 0
    octoberAvg = 0
    novemberAvg = 0
    decemberAvg = 0

    for i in range(31):
        new_line = int(readfile.readline())
        #print(new_line)
        januaryAvg = januaryAvg + new_line

    januaryAvg = round(januaryAvg / 31, 1)
    month_avg.append(januaryAvg)

    #print("JAN", januaryAvg)

    for i in range(28):
        new_line = readfile.readline()
        februaryAvg += int(new_line)

    februaryAvg = round(februaryAvg / 28, 1)
    month_avg.append(februaryAvg)

    for i in range(31):
        new_line = readfile.readline()
        marchAvg += int(new_line)

    marchAvg = round(marchAvg / 31, 1)
    month_avg.append(marchAvg)

    for i in range(30):
        new_line = readfile.readline()
        aprilAvg += int(new_line)

    aprilAvg = round(aprilAvg / 30, 1)
    month_avg.append(aprilAvg)

    for i in range(31):
        new_line = readfile.readline()
        mayAvg += int(new_line)

    mayAvg = round(mayAvg / 31,1)
    month_avg.append(mayAvg)

    for i in range(30):
        new_line = readfile.readline()
        juneAvg += int(new_line)

    juneAvg = round(juneAvg / 30,1)
    month_avg.append(juneAvg)

    for i in range(31):
        new_line = readfile.readline()
        julyAvg += int(new_line)

    julyAvg = round(julyAvg / 31, 1)
    month_avg.append(julyAvg)

    for i in range(31):
        new_line = readfile.readline()
        augustAvg += int(new_line)

    augustAvg = round(augustAvg / 31, 1)
    month_avg.append(augustAvg)

    for i in range(30):
        new_line = readfile.readline()
        septemberAvg += int(new_line)

    septemberAvg = round(septemberAvg /30, 1)
    month_avg.append(septemberAvg)

    for i in range(31):
        new_line = readfile.readline()
        octoberAvg += int(new_line)

    octoberAvg = round(octoberAvg / 31, 1)
    month_avg.append(octoberAvg)

    #print("OCT", octoberAvg)

    for i in range(30):
        new_line = readfile.readline()
        novemberAvg += int(new_line)

    novemberAvg = round(novemberAvg / 30, 1)
    month_avg.append(novemberAvg)

    #print("NOV", novemberAvg)

    for i in range(31):
        new_line = readfile.readline()
        decemberAvg += int(new_line)

    decemberAvg = round(decemberAvg / 31, 1)
    month_avg.append(decemberAvg)

    #print("DEC", decemberAvg)

    #print(month_avg)

    readfile.close()

    write_file = open("steps_by_month.txt", "w")
    write_file.write("{0:<15}|{1:>15}\n".format("Month", "Average"))

    for i in range(len(months)):
        write_file.write("{0:<15}|{1:>15}\n".format(months[i], month_avg[i]))

    write_file.close()


averageSteps()

# Problem 5.
import string
alphabet = string.ascii_lowercase + " .-,!012345678"
key = alphabet[13:] + alphabet[:13]
print(key)


def rot13_encrypt(a_alphabet,a_key):
    plain_text = ""
    encrypt_msg = ""

    readfile = open("file_to_encrypt.txt", "r")


    for aline in readfile:
        plain_text += " " + aline

    readfile.close()

    plain_text.lower()
    #print(plain_text)

    for ch in plain_text:
        idx = a_alphabet.find(ch)
        encrypt_msg += a_key[idx]

    outfile = open("encrypted_msg.txt", "w")
    outfile.write(encrypt_msg)
    outfile.close()

    return encrypt_msg

print(rot13_encrypt(alphabet, key))


def decryption_of_file(a_alphabet, a_key):
    readfile = open("encrypted_msg.txt", "r")
    plain_text = ""
    encrypted_msg = ""

    for aline in readfile:
        encrypted_msg += aline

    readfile.close()

    for ch in encrypted_msg:
        idx = a_key.find(ch)
        print("CH", ch)
        print("idx", idx)
        print(a_alphabet[idx])
        plain_text += a_alphabet[idx]


    return plain_text

print(decryption_of_file(alphabet, key))










