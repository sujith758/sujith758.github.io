drop schema justice cascade;
create schema justice;
create table justice.leauge(County varchar(1200),LicenseNumber varchar(100),OperationType varchar(200),EstablishmentType varchar(1200),EntityName varchar(120),DBAName varchar(200),StreetNumber varchar(200),StreetName varchar(200),AddressLine2 varchar(300),AddressLine3 varchar(2000),City varchar(300),State varchar(200),ZipCode varchar(200),SquareFootage varchar(200),Location varchar(2000));
COPY justice.leauge(County,LicenseNumber,OperationType,EstablishmentType,EntityName,DBAName,StreetNumber,StreetName,AddressLine2,AddressLine3,
City,State,ZipCode,SquareFootage,Location) FROM '/home/sujith/git-repositories/data-import/Retail_Food_stores.csv' DELIMITER ',' CSV HEADER;
create table justice.leauge1(County varchar(1200),LicenseNumber int,OperationType varchar(200),EstablishmentType varchar(1200),EntityName varchar(120),DBAName varchar(200),StreetNumber int,StreetName varchar(200),AddressLine2 varchar(300),AddressLine3 varchar(2000),City varchar(300),State varchar(200),ZipCode int,SquareFootage int,Location varchar(2000));
insert into justice.leauge select(County,Licensenumber,OperationType,EstablishmentType,EntityName,DBAName,cast(StreetNumber as int),StreetName,AddressLine2,AddressLine3,City,State,cast(zipcode as int),cast(squarefootage as int),location) from justice.leauge1;

