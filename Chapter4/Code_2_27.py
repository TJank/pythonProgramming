# How are the following functions implemented
# count, insert

my_list = [1,2,1,2,1,2,3,4,4,4,3,3]
print(my_list)
print(my_list.count(3))

def counter(L, x):
    """
    Function to count the number of times x is in L
    :param L: list
    :param x: element
    :return: count of x in L
    """

    countX = 0
    for e in L:
        if e == x:
            countX += 1

    return countX

print(counter(my_list, 3))


# Creating .insert

my_list.insert(1, "object")
print(my_list)


# Insert:
def insert_v1(L, i, e):
    return L[:i] + [e] + L[i:]

print(insert_v1(my_list, 1, 'object'))




def insert_v2(L, i, e):
    # make a copy of tail of the list starting at i
    tail = L[i:]

    # replace the value at i in L for e
    L[i] = e

    # replace all elements in L with tail elements starting at i + 1
    for j in range(len(tail) - 1):
        L[i + 1] = tail[j]
        i += 1

    # add the last element on the tail to L
    L.append(tail[-1])

insert_v2(my_list, 1, 'object')
print(my_list)


# Shuffle a list
# 1. Select a random index i from the set of indices of a list L
# 2. Remove the element at index i from L and append it to a new list M
# 3. repeat step 2 until L is empty

def shuffle_v1(L):
    from random import randint
    new_list = []
    while not len(L) == 0:
        # slect a random index out of L
        idx = randint(0, len(L) - 1)

        # remove element at index i
        e = L.pop(idx)

        # append element to a new list
        new_list.append(e)

    return new_list


my_list = [i for i in range(10)]
print(my_list)
new_list = shuffle_v1(my_list)
print(new_list)


# Shuffle in place
def shuffle_v2(L, n):
    import random

    for i in range(n):
        # slect a random index out of L
        idx = random.randint(0, len(L)-1)

        # remove element at index i
        e = L.pop(idx)

        # append element to a new list
        new_list.append(e)

my_list = [i for i in range(10)]
print(my_list)
shuffle_v2(my_list, 20)
print(my_list)


# Element Uniqueness : determine if all elements in a collection are unique
# return True if all elements are distinct, False otherwise

def unique(L):
    L.sort()        # sort the list in place

    for i in range(len(L)-1):
        if L[i + 1] == L[i]:
            return False

    return True

my_list = [1,3,5,7,2,8,9,4]
print(unique(my_list))

# Send + More = Money
x = [i for i in range(10)]
for s in x:
    S = s
    for e in x:
        E = e
        for n in x:
            N = n
            for d in x:
                D = d
                for m in x:
                    M = m
                    for o in x:
                        O = o
                        for r in x:
                            R = r
                            for y in x:
                                Y = y
                                # if the assignment is unique continue
                                L = [S, E, N, D, M, O, R, Y]
                                if unique(L):
                                    # check if the selection is a solution
                                    # ...


