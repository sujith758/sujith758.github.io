import psycopg2
import sys
#Passing arguments <csvfile>
arg1 = sys.argv[1]
#Reading the data in csv file
with open(arg1,"r") as myfile:
    data = myfile.read()
lines = data.split("\n")[1:-1]
for line in lines:
    columns = line.split(",")
    print(columns)

#Establishing connection to database
conn = psycopg2.connect("dbname=postgres port=5432 user=postgres password=postgres host=localhost")
cur = conn.cursor()
#Inserting data into table1
postgres_insert_query = """ INSERT INTO public.mapping2(zip,lat,lng,city,state_id,state_name,zcta,parent_zcta,population,density) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
#Creating table2 to load desirable columns
create_table_query = """CREATE TABLE if not exists public.mapping1001(zip varchar(50),city varchar(50),state_id varchar(40),zcta varchar(50))"""
postgres_insert_query1 = """INSERT INTO public.mapping1001(zip,city,state_id,zcta) SELECT zip,city,state_id,zcta from public.mapping2"""
record_to_insert=(columns,)
cur.executemany(postgres_insert_query, record_to_insert)
cur.execute(postgres_insert_query1, create_table_query)
conn.commit()
#Closing connection
cur.close()
conn.close()