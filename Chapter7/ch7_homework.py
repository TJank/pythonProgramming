# Homework 6
# Problem 1. (NEED TUTORING)

# Problem 2.

# Problem 3.

# Problem 4. (NEED TUTORING)

# Problem 5.
problem5_list = [1, 2, (5,9), "bob", [0,0,0], 45, "cat"]
def rotate(a_list, direction):
    removed_el = None
    if direction == "right":
        removed_el = a_list.pop(-1)
        a_list.insert(0, removed_el)

    elif direction == "left":
        removed_el = a_list.pop(0)
        #print(removed_el)
        a_list.append(removed_el)

    return a_list

#print(rotate(problem5_list, "right"))
#print(rotate(problem5_list, "left"))


# Problem 6. (HELP IF TIME)

# Problem 7.
# A. & B. List of lists
class_info = []
info_list = []
readfile = open("studentN_id_gpa.txt", "r")
for aline in readfile:
    #aline.split(",")
    info_list.append(aline.split(","))
    class_info = class_info + info_list

print(info_list)

# Problem 8. (NEED TUTORING)