create database hotel;
use hotel;
create table empl (empid varchar(5) primary key, name varchar(30),
salary int, jobtype varchar(20));
insert into empl values (‘E0001’, ‘Jiya Sharma’, 10000,’receptionist’);
insert into empl values (‘E0002’, ‘Gaurav Gupta’, 10000,’receptionist’);
insert into empl values (‘E0003’, ‘Rahul Srivatava’, 25000,’manager’);
insert into empl values (‘E0004’, ‘ Ching Chang’, 20000,’chef’);
insert into empl values (‘E0005’, ‘Ming Chang’, 15000,’sous chef’);
insert into empl values (‘E0006’, ‘Sing Chang’, 15000,’sous chef’);
insert into empl values (‘E0007’, ‘Poonam Pandey’, 1500,’house
keeping’);
insert into empl values (‘E0008’, ‘komal pandey’, 1500,’house keeping’);
insert into empl values (‘E0009’, ‘Suman Pandey’, 1500,’house
keeping’);
insert into empl values (‘E0010’, ‘Pankaj Ojha’, 1500,’house keeping’);
insert into empl values (‘E0011’, ‘Mickey’, 1450,’waiter’);
insert into empl values (‘E0012’, ‘Sonu’, 1450,’waiter’);
insert into empl values (‘E0013’, ‘Titu’, 1450,’waiter’);

insert into empl values (‘E0014’, ‘Sweety’, 1450,’waitress’);
insert into empl values (‘E0015’, ‘Shambhu Singh’, 2050,’gaurd’);

create table price(Sno int, type varchar(20), cost int);
insert into price values (‘1’, ‘Diamond’, 30000);
insert into price values (‘2’, ‘Emerald’, 25000);
insert into price values (‘3’, ‘Ruby’, 20000);
insert into price values (‘4’, ‘Sapphire’, 15000);
insert into price values (‘5’, ‘Tanzanite’, 10000);

create table comp(Sno int, itemname varchar(30), price int);
insert into price values (‘1’, ‘Soft drinks’, 50);
insert into price values (‘2’, ‘Water bottle’, 70);
Insert into price values (‘3’, ‘cocktail’, 2500);
insert into price values (‘4’, ‘Chocolates’, 100);
insert into price values (‘5’, ‘biscuit’, 50);

create table guests (guestid varchar(30), Name varchar(50), ID_proof
varchar(50), checkin date, checkout date);

insert into guest values(‘G001’, ‘Mohan Das’, ’AADHAR CARD’,’2019-11-
15’,’2019-11-19’);
insert into guest values(‘G002’, ‘Mohi Singh’, ’AADHAR CARD’,’2019-11-
15’,’2019-11-18’);
insert into guest values(‘G003’, ‘Pant Khan’, ’AADHAR CARD’,’2019-11-
15’,’2019-11-160’);
insert into guest values(‘G004’, ‘Joshua’, ’Passport’, ’2019-10-10’,’2019-
10-16’);
insert into guest values(‘G005’, ‘Maria’, ’Passport’, ’2019-10-14’,’2019-
10-16’);
insert into guest values(‘G006’, ‘Alex Hales’, ’Passport’,’2019-10-
13’,’2019-10-16’);
insert into guest values(‘G007’, ‘Alexa’, ’Passport’,’2019-10-12’,’2019-
10-15’);
insert into guest values(‘G008’, ‘Manoj Bajpai’, ’AADHAR CARD’,’2019-
10-12’,’2019-10-15’);

ceate table rooms(guest_id varchar(5) references guest(guestid)
primary key, Type varchar(20), total_people int, extra_bedding
varchar(10), cost int, Room_no int);
insert into rooms values(’G001’,’Tanzanite’, 2, ‘No’, 10000, 104 );
insert into rooms values(’G002’,’Diamond’, 3, ‘No’, 30000, 506);
insert into rooms values(’G003’,’Ruby’, 5, ‘Yes’, 20000, 308 );

insert into rooms values(’G004’,’Ruby’, 1, ‘No’, 20000, 310 );
insert into rooms values(’G005’,’Sapphire’, 2, ‘No’, 15000, 208 );
insert into rooms values(’G006’,’Emerald’, 2, ‘No’, 25000, 420 );
insert into rooms values(’G007’,’Diamond’, 2, ‘No’, 30000, 501 );
insert into rooms values(’G008’,’Emerald’, 4,’Yes’, 25000, 402 );
