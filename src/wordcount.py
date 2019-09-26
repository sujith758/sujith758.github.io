import csv, time
import sys
import os
#Arguments must be added here<filename>
arg1 = sys.argv[1]
if len(sys.argv) < 2:
    print("Please provide input argument:filename")
elif len(sys.argv) > 3:
    print("Index out of range")
    sys.exit()

# To get Elapsed time to read given csv file
def csvReader():
    with open(arg1,"r") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
initialTime = time.time()
cr = csvReader()
finalTime = time.time()
print('The time taken is %s seconds.' % (finalTime - initialTime))

# Current Time and Date
from datetime import datetime
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(timestamp)

# To get given file size in bytes

b = os.path.getsize(arg1)
print(b >> 20)

# To get word count of csv file
with open(arg1,"r") as tetris:
    data = tetris.read()
res = len(data.split("\n"))
print ("The word count is:" +str(res))
