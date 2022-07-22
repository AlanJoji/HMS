/*create database test*/
use test;

create table if not exists Doctor1(
    doc_id char(4) PRIMARY KEY, 
    name varchar(100), 
    ph_no double, 
    speciality varchar(100), 
    e_mail varchar(100)
);

create table if not exists appointment1 (
    D_ID varchar (4),
    P_ID int,
    DTTM date,
    T_Start varchar(5),
    T_End varchar(5),
    foreign key (D_ID) references Doctor1 (doc_id)
);

create table if not exists Patient1(
    reg_no int PRIMARY KEY, 
    name varchar(100), 
    age int(3), 
    gender char(1), 
    bloodgroup varchar(3), 
    email_address varchar(100), 
    ph_no double
);


