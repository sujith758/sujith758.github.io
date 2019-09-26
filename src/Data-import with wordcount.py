import csv, time
import sys
import psycopg2
import os
#Arguments are passed here<filename>
arg1 = sys.argv[1]
#To ensure giving correct arguments
if len(sys.argv) < 2:
    print("Please provide input argument:filename")
    sys.exit()



# To get Elapsed time to read given csv file
def csvReader():
    with open(arg1, "r") as csvfile:
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
with open(arg1, "r") as tetris:
    data = tetris.read()
res = len(data.split("\n"))
print ("The word count is:" + str(res))

# To import data into postgres database by establishing the conn
conn = psycopg2.connect("dbname=state port=5432 user=postgres password=postgres host=localhost")
cur = conn.cursor()
postgres_insert_query = """ INSERT INTO public.elements1(Word_count,File_size,Elapsed_time) VALUES (%s,%s,%s)"""
record_to_insert = (res, b, finalTime)
cur.execute(postgres_insert_query, record_to_insert)
conn.commit()
print("Imported values into postgres database using INSERT command")
cur.close()
conn.close()
