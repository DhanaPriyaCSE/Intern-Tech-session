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
    print("\n\n....*** Driver Registration ***....")
    driver_name=input("\nEnter the your Name:")
    driver_age=input("\nEnter the your Age:")
    driver_license=input("\nEnter the your license Number")
    driver_license_validity=input("\nEnter the your license Validity:")

    return driver_name,driver_age,driver_license,driver_license_validity

def registration_car():
    print("....*** Car Registration ***....")
    car_category=input("\nEnter the car Catogory:")
    car_number=input("\nEnter the Car Number:")
    car_color=input("\nEnter the Car Color")
    car_company=input("\nEnter the Car Company")
    car_model=input("\nEnter the car model")

    return car_category,car_number,car_color,car_company,car_model


def store_registration_details(drivers,cars):
    registration_details=[]
    registration_details.append(drivers)
    registration_details.append(cars)
    return registration_details

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
