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

    def topping(self):
        print("---***IceCream Toppings:***---")
        for topping in self.icecream_toppings:
           print(topping,self.icecream_toppings[topping])
        print("______--****--_______\n")

def cost_flavor_and_type(itype,iflavour,quantity,i):
    i_type=0
    i_flavour=0
    total_cost=0
    if itype in i.icecream_type and iflavour in i.icecream_flavour:
        total_cost=(i.icecream_type[itype]+i.icecream_flavour[iflavour])*quantity
    return total_cost
def bill(cost,itopping,i):
    i_topping=0
    total_bill=0
    if itopping in i.icecream_toppings:
        total_bill=cost+((i.icecream_toppings[itopping])*quantity)
    return total_bill



icecream_type={'stick':60,'cone':40,'cup':20}
icecream_flavour={'chocolate':60,'venila':50,'strawberry':30}
icecream_toppings={'choco chips':30,'caramel':40,'nuts':20}

ice=IceCream(icecream_type,icecream_flavour,icecream_toppings)
ice.print_menu()

itype=input("Enter the type of icream:")
iflavour=input("Enter the flavour of icream:")
quantity=int(input("Enter the Quantity:"))
cost=cost_flavor_and_type(itype,iflavour,quantity,ice)
if iflavour=='chocolate':
   ice.topping()
   itopping=input("Enter the Topping of icream:")
   print(bill(cost,itopping,ice))
else:
    print(cost)
   





        

