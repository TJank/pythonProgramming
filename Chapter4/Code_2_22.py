# Median - "middle" value

def median(data):
    sorted_data = sorted(data)      # if data is orderable, it will be sorted in ascending order

    if not len(data) % 2 == 0:      # odd length
        return sorted_data[len(data)//2]
    else:
        return (sorted_data[len(data)//2 - 1] + sorted_data[len(data)//2]) / 2

ages = [21, 20, 21, 19, 23, 20, 20, 21, 19, 22]
print(median(ages))



# Mode - the most frequent element in the data


def mode(data):
    dictionary_with_counts = dict()

    for item in data:
        if not item in dictionary_with_counts.keys():   #key does not exist
            dictionary_with_counts[item] = 1
        else:
            dictionary_with_counts[item] += 1

    # we still need to find the key with the maximum count in the dictionary
    max_value = max(dictionary_with_counts.values())

    mode_list = []
    for key in dictionary_with_counts.keys():
        if dictionary_with_counts[key] == max_value:
            mode_list.append(key)

    # mode_list = [key for key in dictionary_with_counts.keys() if dictionary_with_counts[key]]

    return mode_list


print(mode(ages))

# Max
def maximum(data):
    value = data[0]

    for i in data:
        if i > value:
            value = i

    return value

# Min
def minimum(data):
    value = data[0]

    for i in data:
        if i < value:
            value = i

    return value

# Standard Deviation
import numpy as np

def std_dev(data):
    # calculate the mean
    x_bar = np.mean(data)

    numerator = 0

    for x in data:
        numerator += (x - x_bar) ** 2

    standard_deviation = np.sqrt(numerator / (len(data) - 1))

    return standard_deviation


data = [20, 21, 22, 19, 20]
print(std_dev(data))
print(np.std(data))


# Generate data using distributions : the uniform, the gauss
from random import gauss, uniform


# Create a list of 1000 numbers in the range 0-50

# approximately using the gauss distribution
mu = 25
sigma = 8
random_list = []
for i in range(1000):
    rand = gauss(25, 5)
    random_list.append(rand)

print(random_list)
print(max(random_list))
print(min(random_list))

# generate numbers using uniform distribution
random_list = []
for i in range(1000):
    rand = uniform(0,50)
    random_list.append(rand)

print(random_list)

# How are the following functions implemented
    










