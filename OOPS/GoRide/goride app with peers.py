import re

class Driver:

    def __init__(self,name,age,license_num,validity_date):
        self.name=name
        self.age=age
        self.license_num=license_num
        self.validity_date=validity_date

    def get_driver_detail(self):
        self.driver_detail="Driver name is "+self.name+"\n Age is "+str(self.age)+"\n license number is "+self.license_num+" and\n validity period is "+self.validity_date
        return self.driver_detail

class Car:

    max_micro=4
    max_xl=10

    def __init__(self,category,number,colour,company,model):
        self.category=category
        self.number=number
        self.colour=colour
        self.company=company
        self.model=model
    def get_car_detail(self):
        self.car_details="Car category is "+self.category+"\n Number is "+self.number+"\n colour is "+self.colour+"\n Company is "+self.company+" and\n model is "+self.model
        return self.car_details



def goride_registration():

    print("*****Welcome To GoRide*****")
    print("\n*****Driver Registration*****\n")
    driver_name=input("Enter the your Name: ")

    while True:
        driver_age=input("Enter the your Age: ")
        if re.match(r"(2)[0-9]",driver_age):
            break
        else:
            print("you are not eligible")

    while True:
        driver_license=input("Enter the your license Number: ")
        if re.match(r"([A-Z]{2}[0-9]{2}(19|20)[0-9][0-9])([0-9]{7})",driver_license):
            break
        else:
            print("License number is not Valid")

    while True:
        driver_license_validity=input("Enter the your license Validity: ")
        if re.match(r"(0?[1-9]|[12][0-9]|3[01])[-](0?[1-9]|1[012])[-]((19|20)[0-9]{2})$",driver_license_validity):
            break
        else:
            print("Enter Valid Expiry date")

    print("\n***** Car Registration*****")

    while True:
        car_category=input("\nEnter the car Category(micro or xl): ")
        if car_category=='micro' or car_category=='xl':
            break
        else:
            print("You are not sucessfully registered in GoRide")
            print("Enter valid category")

    while True:
        car_number=input("Enter the Car Number: ")
        if re.match(r"^[A-Z]{2}\s[0-9]{2}\s[A-Z]{2}\s[0-9]{4}$",car_number):
            break
        else:
            print("Enter valid Car Number")

    car_color=input("Enter the Car Color: ")
    car_company=input("Enter the Car Company: ")
    car_model=input("Enter the car model: ")

    driver_obj=Driver(driver_name,driver_age,driver_license,driver_license_validity)
    car_obj=Car(car_category,car_number,car_color,car_company,car_model)

    return driver_obj.get_driver_detail(),car_obj.get_car_detail()



def store_registration_details():
    registered_details=[]
    registered_details.append(driver_detail)
    registered_details.append(car_detail)
    print("\nSuccessfully registered!!!\n")
    return registered_details

driver_detail,car_detail=goride_registration()
   
print('\n\n'.join(store_registration_details()))


'''
*****Welcome To GoRide*****

*****Driver Registration*****

Enter the your Name: priya
Enter the your Age: 23
Enter the your license Number: TN1420110062672
Enter the your license Validity: 06-02-2022

***** Car Registration*****

Enter the car Category(micro or xl): micro
Enter the Car Number: TN 01 PA 6545
Enter the Car Color: black
Enter the Car Company: aadi
Enter the car model: a5

Successfully registered!!!

Driver name is priya
Age is 23
license number is TN1420110062672 and
validity period is 06-02-2022

Car category is micro
Number is TN 01 PA 6545
colour is black
Company is aadi and
model is a5

'''
