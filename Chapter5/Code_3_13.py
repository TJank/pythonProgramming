# COPIED OVER FROM CODE_3_1 (GUARIO'S DIDN'T WORK)
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

#print(magnitudes)
#print(len(magnitudes))

# Numpy module to compute descriptive statistics
import numpy as np

mags_mean = np.mean(magnitudes)
mags_median = np.median(magnitudes)
mags_std = np.std(magnitudes)

# Draw a histogram of the data using Matplotlib
import matplotlib.pyplot as plt
# n is how many "buckets" or things to store data
n = 50

#plt.hist(magnitudes, n, color="green")

#plt.axvline(mags_mean, color="red", linestyle="dashed")
#plt.axvline(mags_mean + mags_std, color="yellow", linestyle="dashed")
#plt.axvline(mags_mean - mags_std, color="yellow", linestyle="dashed")

#plt.ylabel("Count")
#plt.xlabel("Magnitudes")
##plt.title(r'Histogram of Eathquake Magnitueds: $\mu=$'\
##          + str(mags_mean) + ', $\sigma=$' + str(mags_std))

#plt.title(r'Histogram of Earthquake Magnitudes:' + \
         # r'$\mu=$ {0:.2f}, $\sigma=$ {1:.2f}'.format(mags_mean, mags_std))

#plt.show()




# Temperature Converstion example
def celsius_to_fahrenheit(C):
    F = C * (9/5) + 32
    return F

#celsius_list = []
#for i in range(-300, 301):
#    celsius_list.append(i)

celsius_list = [i for i in range(-300, 301)]

#print("{0:<15}|{1:>15}".format("Celsius", "Fahrenheit"))

# Output results to a file
# when opening a file with W : if the file does not exist it will be created
# if it is created, it will be flushed and overwritten

#out_file = open("temperatures.txt", "w")
#out_file.write("{0:<15}|{1:>15}\n".format("Celsius", "Fahrenheit"))
#for c in celsius_list:
#    out_file.write("{0:<15.2f}|{1:>15.2f}\n".format(c, celsius_to_fahrenheit(c)))

#out_file.close()






# String Formatting
# Two ways to format a string

# 1. Using the .format() function
print("This is the number {0} and this is the letter {1}".format(1, "A"))
print("THis is the tuple {0} amd this is the list {1}".format((1,2), [1,2]))


# 2. Using the % symbol (see book)
print("This is the number %i and this is the letter %c" % (1, "A"))




# Pearson Correlation Coefficient
y = [200.3, 300.1, 100.2]
x = [1.2, 3.5, 2.7]

def pearson_correlation(x_data, y_data):
    """The size of the x_data and y_data must be the same."""
    x_bar = np.mean(x_data)
    y_bar = np.mean(y_data)

    n = len(x_data)

    x_std = np.std(x_data)
    y_std = np.std(y_data)

    numerator = 0
    for i in range(n):
        numerator += (x_data[i] - x_bar) * (y_data[i] - y_bar)

    denominator = (n - 1) * x_std * y_std

    p = numerator / denominator
    return p

p = pearson_correlation(x, y)
print(p)

# Compare data values from two different stocks
# Apple - AAPL
# Nvidia - NVDA

apple_closing_stock = []
path_to_file = "C:\\Users\\tyler\\Downloads\\"
file_name = "AAPL.csv"

in_file = open(path_to_file + file_name, "r")

in_file.readline()
for line in in_file:
    new_line = line.split(",")
    closing_stock = float(new_line[4])
    apple_closing_stock.append(closing_stock)
    #apple_closing_stock.append(float(line.split(",")[4]))




nvidia_closing_stock = []
path_to_nvidia = "C:\\Users\\tyler\\Downloads\\"
f_name = "NVDA.csv"

nvidia_in_file = open(path_to_nvidia + f_name, "r")

nvidia_in_file.readline()
for line in nvidia_in_file:
    nvidia_closing_stock.append(float(line.split(",")[4]))

in_file.close()
nvidia_in_file.close()


print(apple_closing_stock)
print("-"*20)
print(nvidia_closing_stock)

#print(pearson_correlation(apple_closing_stock, nvidia_closing_stock))








