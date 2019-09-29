import psycopg2
# import sys
# arg1 = sys.argv[1]

with open('/home/sujith/Documents/uszips1.csv') as myfile:
    data = myfile.read()
lines = data.replace("\"","\'").split("\n")[1:3]
for line in lines:
    columns = line.split("\n")
    print(columns)
conn = psycopg2.connect("dbname=postgres port=5432 user=postgres password=postgres host=localhost")
cur = conn.cursor()
postgres_insert_query = """ INSERT INTO public.mapping2(zip,lat,lng,city,state_id,state_name,zcta,parent_zcta,population,density) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
record_to_insert = (columns)
cur.executemany(postgres_insert_query, record_to_insert)
conn.commit()
cur.close()
conn.close()

