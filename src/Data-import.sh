#!/bin/bash
export PGPASSWORD=postgres
filemane=$1
#To get csv column count
CSVCNT=`wc -l "$filename" | cut -d " " -f 1`
echo "CSV COUNT: $CSVCNT"

#Establishing connection to database
psql -h localhost -p 5432 -d postgres -U postgres -f Listofstores.sql
CNT=`psql -h localhost -p 5432 -d postgres -U postgres -t -q -c 'select count(*) from justice.leauge;'`
echo "COUNT: $CNT"
CNT=${CNT//[[:space:]]/}

echo "Count of columns : $CNT"
