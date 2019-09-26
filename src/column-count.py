import sys

#Arguments are passed here <filename><column1>
arg1 = sys.argv[1]
arg2 = sys.argv[2]

#To ensure that arguments are passed
if len(sys.argv) < 2:
    print("Please provide input argument:filename,column1")
elif len(sys.argv) > 3:
    print("Index out of range")
    sys.exit()

# Reading the data in csv file
with open(arg1, "r") as csvfile:
    data = csvfile.read()
lines = data.split()
# Indexing is given to header line in order to search by header
header = lines[0].replace("\"", "")
columns = header.split(",")
# print("index of given column", columns.index(arg2))
columnindex = columns.index(arg2)

# Reading data again to get access to information ignoring header
with open(arg1, "r") as csvfile:
    data = csvfile.read().replace("\"", "")
    lines = data.split("\n")[1:]
    # List is created and data is loaded into list
    mylist = list()
    for line in lines:
        c1 = line.split(",")[columnindex]
        mylist.append(c1)
        # To get count
    print("count of column", arg2, "is ", len(mylist))
