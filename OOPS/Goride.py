import re

class Driver:
    def __init__(self,driver_name,driver_age,driver_license,driver_license_validity):
        self.driver_name=driver_name
        self.driver_age=driver_age
        self.driver_license=driver_license
        self.driver_license_validity=driver_license_validity


    def get_driver_details(self):
        return (self.driver_name,self.driver_age,self.driver_license,self.driver_license_validity)


class Car:
    def __init__(self,catogory,car_number,car_color,car_company,car_model):
        self.catogory=catogory
        self.car_number=car_number
        self.car_color=car_color
        self.car_company=car_company
        self.car_model=car_model

    def get_car_details(self):
        return (self.catogory,self.car_number,self.car_color,self.car_company,self.car_model)

def registration_driver():
    print(" Welcome to GoRide!!!")
    print("\n....*** Driver Registration ***....")
    while True:
        driver_name=input("Enter the your Name:")
        if re.match(r"[A-Za-z]",driver_name):
            break
        else:
            print("you are not eligible")
    while True:
        driver_age=input("Enter the your Age:")
        if re.match(r"(2)[0-9]",driver_age):
            break
        else:
            print("you are not eligible")
        
    while True:
        driver_license=input("Enter the your license Number:")
        if re.match(r"([A-Z]{2}[0-9]{2}(19|20)[0-9][0-9])([0-9]{7})",driver_license):
            break
        else:
            print("License number is not Valid")
    while True:
        driver_license_validity=input("Enter the your license Validity:")
        if re.match(r"(0?[1-9]|[12][0-9]|3[01])[-](0?[1-9]|1[012])[-]((19|20)[0-9]{2})$",driver_license_validity):
            break
        else:
            print("Enter Valid Expiry date")
    

    

    return driver_name,driver_age,driver_license,driver_license_validity

def registration_car():
    print("....*** Car Registration ***....")
    while True:
        car_category=input("\nEnter the car Category(micro or XL:)")
        if car_category=='micro' or car_category=='XL':
            break
        else:
            print("Enter valid category")
    while True:
        car_number=input("\nEnter the Car Number:")
        if re.match(r"^[A-Z]{2}\s[0-9]{2}\s[A-Z]{2}\s[0-9]{4}$",car_number):
            break
        else:
            print("Enter valid Car Number")
    car_color=input("Enter the Car Color:")
    car_company=input("Enter the Car Company:")
    car_model=input("Enter the car model:")

    return car_category,car_number,car_color,car_company,car_model


def store_registration_details(drivers,cars):
    registration_detail=[]
    registration_detail.append(drivers)
    registration_detail.append(cars)
    print("\n\nregistration Sucessfull!!")
    return registration_detail


'''
    for driver in drivers:
        if driver_license==driver.driver_license:
                print("license_number already exists")
        else:
                print("Register Sucessfull");
    
'''


(driver_name,driver_age,driver_license,driver_license_validity)=(registration_driver())
(car_category,car_number,car_color,car_company,car_model)=(registration_car())

drivers=Driver(driver_name,driver_age,driver_license,driver_license_validity)
cars=Car(car_category,car_number,car_color,car_company,car_model)

                
store_registration_details(drivers,cars)

'''
 Welcome to GoRide!!!

....*** Driver Registration ***....
Enter the your Name:Bama
Enter the your Age:21
Enter the your license Number:TN1420110062821
Enter the your license Validity:04-02-2021
....*** Car Registration ***....

Enter the car Category(micro or XL):XL

Enter the Car Number:TN 01 PA 4554
Enter the Car Color:black
Enter the Car Company:honda
Enter the car model:city

registration Sucessfull!!

'''
