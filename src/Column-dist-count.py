import sys
#Passing arguments
arg1 =sys.argv[1]
arg2 =sys.argv[2]
# Reading the data in csv file
with open(arg1, "r") as csvfile:
    data = csvfile.read()
lines = data.split()
# Indexing is given to header line in order to search by header
header = lines[0].replace("\"", "")
columns = header.split(",")
# print("index of given column", columns.index(arg2))
columnindex = columns.index(arg2)

#Reading data again to get access to information ignoring header
with open(arg1, "r") as csvfile:
    data = csvfile.read().replace("\"", "")
    lines = data.split("\n")[1:]
    # List is created and data is loaded into list
    mylist = list()
    for line in lines:
        c1 = line.split(",")[columnindex]
        mylist.append(c1)
        # To get distinct count
        myset = set(mylist)
    print("distinct count of column", arg2, "is ", len(myset))
