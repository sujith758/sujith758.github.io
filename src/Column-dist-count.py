import os.path
#By using relative path to open the csv file
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/uszips.csv")
# Arguments are passed here
arg1 = path
arg2 = "zip"
arg3 = "00601"
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
