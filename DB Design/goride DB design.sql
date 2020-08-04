create database Goride;

create schema Goride;

tblDrivers:

create table Goride.tblDrivers(
			driverId int AUTO_INCREMENT primary key,
			name varchar not null,
 			age int not null,
			licenseNumber varchar not null unique key,
			validityPeriod date not null);

tblDriverVehicleTypes:

create table Goride.tblDriverVehicleTypes(
			vehicleTypeId int AUTO_INCREMENT primary key,
			categoryName varchar not null  
			);

tblvehicles:

create table Goride.tblvehicles(vehicleId int AUTO_INCREMENT primary key, 			
				vehicleNumber varchar unique Key,
				color varchar not null,
				model varchar not null,
				driverId  int Foreign key References tblDrivers(driverId),
				vehicleTypeId int Foreign key References tblDriverVehicleTypes(vehicleTypeId )				
			);

tblvehicleCompanies:
create table Goride.tblvehicleCompanies(comapnyId int AUTO_INCREMENT primary key, 
				      companyName varchar not null,
				      vehicleId int Foreign key References tblvehicles(vehicleId )
				     );

tblPrices:
create table Goride.tblprices(priceID int AUTO_INCREMENT primary key,
			     acPrice int not null,
			     non_acPrice int not null,
			     min_range int not null,
			     max_range int not null,
			     vehicleTypeId int Foreign key References tblDriverVehicleTypes(vehicleTypeId )					
			     );

tblbookings:

create table Goride.tblbookings(bookingid int not null primary key AUTO_INCREMENT,
				selecetedCategory varchar not null,
				ac_r_not varchar not null,
				price int not null,
				range int not null,
				);