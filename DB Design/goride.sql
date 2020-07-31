
create database Goride;

create schema Goride;

tblDrivers:

create table tblDrivers(name varchar not null,
 			age int not null,
			licenseNumber varchar not null primary key,
			validityPeriod date not null);

tblvehicles:

create table tblvehicles(category varchar not null,
			vehicleNumber varchar not null primary key,
			color varchar null,
			company varchar not null ,
			model varchar not null,
			maximumPPL int not null,
			licensenumber varchar,
			FOREIGN KEY (licensenumber) REFERENCES tbldrivers(licensenumber)
			)

tblrides:

create table tblrides(  rideid int not null ,
			category varchar not null,
			vehicleNumber varchar not null,
			minrange int not null,
			maxrange int not null,
			priceWidAc int not null,
			priceWidNonAC int not null,
			FOREIGN KEY (vehicleNumber) REFERENCES tblvehicles(vehicleNumber)
			primary key(rideid,category)
			)					