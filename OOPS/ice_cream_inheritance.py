class IceCream:
    def __init__(self):
        self.icecream_type={'stick':60,'cone':40,'cup':20}
        self.icecream_flavour={'chocolate':60,'venila':50,'strawberry':30}
        self.icecream_toppings={'choco chips':30,'caramel':40,'nuts':20}
    
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



class TotalCost(IceCream):
    def __init__(self,i_type,i_flavor,i_topping,quantity):
        self.i_type=i_type
        self.i_flavor=i_flavor
        self.i_topping=i_topping
        self.quantity=quantity
        super().__init__()
    def total_cost(self):
         i_type=0
         i_flavor=0
         i_topping=0
         total_cost=0
         if i_type in icecream_type and i_flavour in icecream_flavour and i_topping in icecream_toppings:
            total_cost=(icecream_type[i_type]+icecream_flavour[i_flavour]+icecream_toppings[i_topping])*quantity
         else:
            print("Enter Proper Input")
         return("The total cost is:",total_cost)
         
'''
icecream_type={'stick':60,'cone':40,'cup':20}
icecream_flavour={'chocolate':60,'venila':50,'strawberry':30}
icecream_toppings={'choco chips':30,'caramel':40,'nuts':20}
'''

ice=IceCream()
ice.print_menu()

itype=input("Enter the type of icream:")
iflavour=input("Enter the flavour of icream:")
itopping=input("Enter the Topping of icream:")
quantity=int(input("Enter the Quantity:"))


cream=TotalCost(itype,iflavour,itopping,quantity)
cream.total_cost()








                        
