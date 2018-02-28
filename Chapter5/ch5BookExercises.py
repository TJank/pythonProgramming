# Ch 5 pg 158

# Reading text file in python
#rainfile = open("rainfall.txt", "r")

#for aline in rainfile:
   # values = aline.split()
    #print(values[0], "had ", values[1], " inches of rain.")

#rainfile.close()

# Listing 5.2 pg 160
rainfile = open("rainfall.txt", "r")
outfile = open("rainfallInCM.txt", "w")

for aline in rainfile:
    values = aline.split()

    inches = float(values[1])
    cm = 2.54 * inches

    outfile.write(values[0]+" "+str(cm)+"\n")

rainfile.close()
outfile.close()

# Session 5.3 pg 163
a = 10
b = 'apple'

print("The %s costs %d cents." % (b,a))
myStr = "The %+15s costs %4.1d cents" % (b,a)
print(myStr)

myDict = {'name' : 'apple', 'cost' : 10, 'price' : 15}
print("The %(name)s costs %(price)5.1f cents" % myDict)

tempConvFile = open("tempconv.txt", "w")

tempConvFile.write("Fahrenheit" + "  to  " + "Celsius")
for temp in range(-300, 212):
    new_temp = (temp - 32) * (5/9)

    tempConvFile.write("%d F       %d  \n" % (temp, new_temp))

tempConvFile.close()

# Listing 5.3 PG 167
def makeMagnitudeList():
    quakefile = open("earthquakes.txt", "r")

    maglist = []
    for aline in quakefile:
        vlist = aline.split()
        maglist.append(float(vlist[0]))
    return maglist

print(makeMagnitudeList())










