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













