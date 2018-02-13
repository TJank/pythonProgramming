# Tuples - immutable ordered collection of objects

# empty Tuple
t1 = tuple()

# Simple tuple examples
t2 = 1, 2
t3 = 1.5, 'a', 3

print(t2)
print(t3)

# Indexing
t4 = 1.5, 'cat', (3, 5, 6), 8
#print(t4[2][1]) # DOUBLE INDEXING
t6 = t4[2][1]
print(t6)   # not a tuple anymore

t7 = t4[1][2]
print(t7)


# slicing
t8 = t4[1:3]
print(t8)


# COncatenation
t9 = t4 + t8
print(t9)




# DICTIONARIES - mutable unordered collections of key:value pairs (JSON) :)

# Example
d1 = {1:"A", 2: "B", "C": 3, (1, 2): "cat", 1.5: (1, 2, 3, "hello")}
print(len(d1))

# Indexing: use keys to index dictionaries
v1 = d1[1]
print(v1)

v2 = d1[2]
print(v2)

print(d1["C"])

keys = d1.keys()
print(keys)

print(d1[1, 2])
print(d1[1.5][3])














