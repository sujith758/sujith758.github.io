#!/bin/bash
export PGPASSWORD=$PGPASSWORD
filename=$1
PGPASSWORD=$2
if [[ len($filename) < 2 ]]; then 
	echo "Please provide input arguments:filename,password"
fi
#To get csv column count
CSVCNT=`wc -l "$filename" | cut -d " " -f 1`
echo "CSV COUNT: $CSVCNT"

#Establishing connection to database
psql -h localhost -p 5432 -d state -U postgres -f Data-import-sql.sql
CNT=`psql -h localhost -p 5432 -d postgres -U postgres -t -q -c 'select count(*) from justice.leauge;'`
echo "COUNT: $CNT"
CNT=${CNT//[[:space:]]/}

echo "Count of columns : $CNT"
