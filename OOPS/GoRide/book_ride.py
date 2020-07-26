class GoRideBook:
    def __init__(self,category,ride_range,price_ac,price_n_ac,ac_r_not):
        self.category=category
        self.ride_range=ride_range
        self.price_ac=price_ac
        self.price_n_ac=price_n_ac
        self.ac_r_not=ac_r_not
    def get_category(self):
        return self.category
    
    def get_price_ac(self):
        return self.price_ac
    
    def get_price_non_ac(self):
        return self.price_n_ac
    
    def is_ac_r_not(self):
        return self.ac_r_not
            
def is_category_available(selected_category):
    filtered_category = next((selected_category for gorider in goriders if gorider.category.lower() ==selected_category ),None)
    return filtered_category


def display_selection_details(goriders):
    print("GoRide available Rides:")
    print("Category\tRide Range\tPrice_with_AC\tprice_without_AC")
    for gorider in goriders:
        print(gorider.category+"\t\t"+gorider.ride_range+"\t\t"+str(gorider.price_ac)+"\t\t"+str(gorider.price_n_ac))


def get_user_wish_ride():
    selected_category=input("Select category(auto,micro,xl)").lower()
    category=is_category_available(selected_category)
    if category is None:
        print("Enter valid choice")
    selected_km=int(input("Enter the traveling km:"))
    select_ac_r_not=input("Do u want ac r not? yes/no").lower()
    if selected_category=='auto':
        cost=calculate_auto_cost(selected_category,selected_km,select_ac_r_not)
            
    elif selected_category=='micro':
         cost=calculate_micro_cost(selected_category,selected_km,select_ac_r_not)
    elif selected_category=='xl':
         cost=calculate_micro_cost(selected_category,selected_km,select_ac_r_not)
    else:
        pass
    print("total cost",cost)
        
def calculate_auto_cost(selected_category,selected_km,select_ac_r_not):
    total_cost=0
    km=selected_km
    if select_ac_r_not=='yes':
        if km<=15:
            total_cost = km*10
        elif 15<km<30:
            total_cost = km*8
        elif km>30:
            total_cost = km*15
        else:
            pass
    else:
        print("For Auto without Ac is not available")
    return total_cost

def calculate_micro_cost(selected_category,selected_km,select_ac_r_not):
    total_cost=0
    km=selected_km
    if select_ac_r_not=='yes':
        if km<=15:
           total_cost = km*12
        elif km>=15:
            total_cost = km*10
        else:
             pass
    else:
        if km<=15:
           total_cost = km*14
        elif km>=15:
             total_cost = km*12
        else:
             pass
            
    return total_cost

def calculate_xl_cost(selected_category,selected_km,select_ac_r_not):
    total_cost=0
    km=selected_km
    if select_ac_r_not=='yes':
        if km<=15:
           total_cost = km*14
        elif km>=15:
            total_cost = km*14
        else:
             pass
    else:
        if km<=15:
           total_cost = km*15
        elif km>=15:
             total_cost = km*15
        else:
             pass

    return total_cost
    

auto_15km=GoRideBook('Auto','upto 15km',10,'NA','yes')
auto_30km=GoRideBook('Auto','15 - 30km',8,'NA','yes')
auto_above_30km=GoRideBook('Auto','30 and above',15,'NA','yes')
micro_15km=GoRideBook('Micro','upto 15km',12,14,'yes')
micro_above_15km=GoRideBook('Micro','15 and above',10,12,'yes')
xl_15km=GoRideBook('XL','Upto 15km',14,15,'yes')
xl_above_15km=GoRideBook('XL','above 15km',14,15,'yes')

goriders=[auto_15km,auto_30km,auto_above_30km,micro_15km,micro_above_15km,xl_15km,xl_above_15km]
display_selection_details(goriders)

get_user_wish_ride()


