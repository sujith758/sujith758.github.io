import csv
import sys
#Arguments are passed here
arg1 = sys.argv[1]
arg2 = sys.argv[2]
#Reading the csv file
with open(arg1, "r") as csvfile:
    data = csvfile.read()
    lines = data.split(",")
#Loading the first column into dictionary
d = [lines[0]]

re = {}
for item in d:
    if (item in re):
        re[item] += 1
    else:
        re[item] = 1
columnindex = item.index(arg2)
#Reading the file again to retrieve data
with open(arg1, "r") as csvfile:
    data = csvfile.read()
    lines = data.split("\n")[1:]
#List is created and data is loaded into list 
    mylist = list()
    for line in lines:
        c1 = line.split(",")[columnindex]
        mylist.append(c1)
#getting results
    print("count of column:", arg2, "is ", len(mylist))
