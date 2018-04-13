# QUIZ CODE

list = [4,7,8,2,3,1,5,6]

def arrange(list, k):
    element_idx = list.index(k)
    #print(mid_element)

    for i in range(len(list)):
        if list[i] < k:
            pop = list.pop(list[i])
            list.insert(i, pop)
        elif list[i] > k:
            pop = list.pop(list[i])
            list.append(pop)

    return l


#print(arrange(list, 7))

def reorder(a_list, k):
    # find k and put it in a new list
    idx = a_list.index(k)

    # put k in a new list and remove it from a_list
    temp_list = [a_list.pop(idx)]

    # remove elements from a_list one by one and put them in temp_list
    # in the right position

    for i in range(len(a_list)):
        if a_list[0] > k:
            temp_list.append(a_list.pop(0))
        else:
            temp_list.insert(0, a_list.pop(0))

    for i in temp_list:
        a_list.append(i)

reorder(list, 6)
print(list)


# Given integer assignments to variables, how can you convert a string to an int
# For example
# S = 6
# E = 5
# N = 7
# D = 1

# How do we convert SEND as a string and then to an int so that we end up with 6571 as an integer
# S + E + N + D = 19 not 6571
# Trick is to use the .join() function on strings
# The following statement will join a list of strings with a given separator
S, E, N, D = 6, 5, 7, 1
send = int(''.join([str(S), str(E), str(N), str(D)]))
print(send)


# Plotting Data and managing files

# Step 1: open a file to read data
# open/close files commands
# open == takes a file and puts that file in memory
in_file = open("earthquakes.txt" , "r")     # "r" = readonly, "w" = flush and write, "a" = append, starts at the end

in_file.readline()      # read the first line (a single line) and returns it as a string

magnitudes = []

# Step 2: read data from the file
for line in in_file:
    new_line = line.split()     # Creates a list of string items seperated by spaces(default)
    magnitudes.append(float(new_line[0]))

in_file.close()

print(magnitudes)
print(len(magnitudes))









