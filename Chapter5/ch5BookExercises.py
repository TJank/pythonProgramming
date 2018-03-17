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
    quakefile.readline()

    maglist = []
    for aline in quakefile:
        vlist = aline.split()
        maglist.append(float(vlist[0]))
    return maglist

#print(makeMagnitudeList())

magList = makeMagnitudeList()
#print(max(magList))

def group_magnitudes(list):
    groupDict = {'micro' : 0, 'minor' : 0, 'light' : 0, 'moderate' : 0, 'major' : 0, 'strong' : 0, 'great' : 0}

    for mag in list:
        if mag <= 3:
            groupDict['micro'] = groupDict['micro'] + 1
        elif mag >= 3 and mag <= 3.9:
            groupDict['minor'] = groupDict['minor'] + 1
        elif mag >= 4 and mag <= 4.9:
            groupDict['light'] = groupDict['light'] + 1
        elif mag >= 5 and mag <= 5.9:
            groupDict['moderate'] = groupDict['moderate'] + 1
        elif mag >= 6 and mag <= 6.9:
            groupDict['major'] = groupDict['major'] + 1
        elif mag >= 7 and mag <= 7.9:
            groupDict['strong'] = groupDict['strong'] + 1
        elif mag >= 8:
            groupDict['great'] = groupDict['great'] + 1

    return groupDict

#print(group_magnitudes(magList))

# Session 5.7 PG 172
#import urllib.request
#page = urllib.request.urlopen("http://knuth.luther.edu/`david/helloworld.html") # ERROR

# Listing 5.4 PG 175
import urllib.request

def countHead(url):
    page = urllib.request.urlopen(url)
    numHeadLines = 0

    line = page.readline().decod('utf-8')
    while '<head>' not in line:
        line = page.readline().decode('utf-8')

    line = page.readline().decode('utf-8')
    while '</head>' not in line:
        numHeadLines = numHeadLines + 1
        line = page.readline().decode('utf-8')

    line = page.readline().decode('utf-8')
    while '<body>' not in line:
        line = page.readline().decode('utf-8')

    line = page.readline().decode('utf-8')
    while line != "" and "</body>" not in line:
        print (line[:-1])
        line = page.readline().decode('utf-8')

    print ("number of lines in header = ", numHeadLines)

    page.close()

# DO CHAPTER 5 EXERCISES PG 175-176


# SESSION 5.8 pg 177 (ERROR : ichar.yahoo.com NO LONGER EXISTS)
#url1 = urllib.request.urlopen('http://ichart.yahoo.com/table.csv?s=TGT')
#data = url1.readlines()[:10]
#print(data)


# LIsting 5.5 The book's Pearson Correlation Function pg 179
from numpy import std
def correlation(xlist, ylist):
    xbar = mean(xlist)
    ybar = mean(ylist)
    xstd = std(xlist)
    ystd = std(ylist)
    num = 0
    for i in range(len(xlist)):
        num = num + (xlist[i] - xbar) * (ylist[i] - ybar)
    corr = num / ((len(xlist)- 1) * xstd * ystd)
    return corr


# Listing 5.6 pg 182
def stockCorrelate(ticker1, ticker2):
    url1 = urllib.request.urlopen("ENTER A VALID URL")
    url2 = urllib.request.urlopen("ENTER A SECOND VALID URL")

    t1Data = url1.readlines()
    t2Data = url2.readlines()
    t1Data = [line[0:-1].decode('utf-8').split(',') for line in t1Data[1:]]
    t2Data = [line[0:-1].decode('utf-8').split(',') for line in t2Data[1:]]
    t1Close = []
    t2Close = []
    for i in range(min(len(t1Data), len(t2Data))):
        if t1Data[i][0] == t2Data[i][0]:
            t1Close.append(float(t1Data[i][4]))
            t2Close.append(float(t2Data[i][4]))

    return correlation(t1Close, t2Close)

