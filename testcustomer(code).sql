create database test


create database pharmacy
drop database pharmacy
create  database pharmacy
create table customer(
Id int primary key,
Name varchar(50) not null,
Age tinyint check (age>=15 and age<=90),
Phone int unique,

Addresess varchar(50) not null,
Email varchar(50) unique) 
drop table customer
drop database pharmacy
