class IceCream:
    def __init__(self,icecream_type,icecream_flavour,icecream_toppings):
        self.icecream_type=icecream_type
        self.icecream_flavour=icecream_flavour
        self.icecream_toppings=icecream_toppings
    
    def print_menu(self):
        print("_____IceCream Menu_______\n")
        print("______--****--_______\n")
        for type_ice in self.icecream_type:
            print("Type of IceCreams:",type_ice)
            for flavour in self.icecream_flavour:                 
                 print(flavour,(int(self.icecream_flavour[flavour]))+(int(self.icecream_type[type_ice])))
            print("______--****--_______\n")
                 
        print("---***Ice Cream Toppings:***---")
        for topping in self.icecream_toppings:
            print(topping)
        print("______--****--_______\n")


'''
class TotalCost(IceCream):
    def __init__(self,i_type,i_flavor,i_topping,quantity):
        self.i_type=i_type
        self.i_flavor=i_flavor
        self.i_topping=i_topping
        self.quantity=quantity
        super().__init__(icecream_type,icecream_flavour,icecream_toppings)
    def total_cost(self):
         i_type=0
         i_flavor=0
         i_topping=0
         total_cost=0
         if i_type in IceCream(self).icecream_type and i_flavour in IceCream(self).icecream_flavour and i_topping in IceCream(self).icecream_toppings:
            total_cost=(IceCream(self).icecream_type[i_type]+IceCream(self).icecream_flavour[i_flavour]+IceCream(self).icecream_toppings[i_topping])*quantity
         else:
            print("Enter Proper Input")
         print("The total cost is:",total_cost)
'''

def total_cost(itype,iflavour,itopping,quantity,i):
    i_type=0
    i_flavor=0
    i_topping=0
    if itype in i.icecream_type and iflavour in i.icecream_flavour and itopping in i.icecream_toppings:
        total_cost=(i.icecream_type[itype]+i.icecream_flavour[iflavour]+i.icecream_toppings[itopping])*quantity
    else:
        print("Enter Proper Input")
    print("The total cost is:",total_cost)



icecream_type={'stick':60,'cone':40,'cup':20}
icecream_flavour={'chocolate':60,'venila':50,'strawberry':30}
icecream_toppings={'choco chips':30,'caramel':40,'nuts':20}
        
ice=IceCream(icecream_type,icecream_flavour,icecream_toppings)
ice.print_menu()

itype=input("Enter the type of icream:")
iflavour=input("Enter the flavour of icream:")
itopping=input("Enter the Topping of icream:")
quantity=int(input("Enter the Quantity:"))


total_cost(itype,iflavour,itopping,quantity,ice)

'''
cream=TotalCost(itype,iflavour,itopping,quantity)

'''






                        
