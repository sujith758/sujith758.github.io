#!/bin/bash
#Establishing the connection to database
export PGPASSWORD=postgres
psql -h localhost -p 5432 -d state -U postgres -f sh groupby-column-sql.sql
CNT=`psql -h localhost -p 5432 -d postgres -U postgres -t -q -c 'select count(Zipcode) from justice.leauge;'`
echo "count of column is :$CNT "
