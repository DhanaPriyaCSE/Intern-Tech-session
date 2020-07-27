class Auto:
    def __init__(self,category,ride_range,price_wid_ac,price_non_ac,is_ac_r_not):
        self.category=category
        self.ride_range=ride_range
        self.price_wid_ac=price_wid_ac
        self.price_non_ac=price_non_ac
        self.is_ac_r_not=is_ac_r_not
        self.member_size=3

    def auto_ac_price(self):
        return self.price_wid_ac

class Micro:
    def __init__(self,category,ride_range,price_wid_ac,price_non_ac,is_ac_r_not):
        self.category=category
        self.ride_range=ride_range
        self.price_wid_ac=price_wid_ac
        self.price_non_ac=price_non_ac
        self.is_ac_r_not=is_ac_r_not
        self.member_size=4

    def auto_ac_price(self):
        return self.price_wid_ac,self.ride_range

    def auto_non_ac_price(self):
        return self.price_non_ac,self.ride_range

class XL:
    def __init__(self,category,ride_range,price_wid_ac,price_non_ac,is_ac_r_not):
        self.category=category
        self.ride_range=ride_range
        self.price_wid_ac=price_wid_ac
        self.price_non_ac=price_non_ac
        self.is_ac_r_not=is_ac_r_not
        self.member_size=10

    def auto_ac_price(self):
        return self.price_wid_ac
    
    def auto_non_ac_price(self):
        return self.price_non_ac

class Ride:
    def __init__(self,category,ac_r_not,select_range):
        self.category=category
        self.ac_r_not=ac_r_not
        self.select_range=select_range
    def book_ride(self):
        book_ride=[]
        book_ride.append((self.category,self.ac_r_not,self.select_range))
        print("your Ride Booked Sucessfully!!!")


def is_category_available(selected_category):
    filtered_category = next((selected_category for gorider in goriders if gorider.category.lower() ==selected_category ),None)
    return filtered_category


def display_price_menu(objects,category,ac_r_not):
    print("category\triderange\tprice\tMember size")
    for obj in objects:
        if ac_r_not=='yes':
            print(obj.category+'\t\t'+obj.ride_range+'\t'+str(obj.price_wid_ac)+'\t'+str(obj.member_size))
        else:
            if category!='auto':
              print(obj.category+'\t\t'+obj.ride_range+'\t'+str(obj.price_non_ac)+'\t'+str(obj.member_size))
            else:
                print("Without AC is not available")
                break

def user_selection(auto,micro,xl):
    print("....****..Welcome to GoRide..***....\nAvailable categories\nAuto\tMicro\tXL")
    category=input("Select category u want to ride:").lower()
    selected_category=is_category_available(category)
    if selected_category is None:
       print("please Select only available choice")
    ac_r_not=input("Do u want ac category?(yes/no)").lower()
    if category=='auto':
        display_price_menu(auto,category,ac_r_not)
    elif category=='micro':
        display_price_menu(micro,category,ac_r_not)
    elif category=='xl':
        display_price_menu(xl,category,ac_r_not)
    else:
        pass

    select_range=input("select ur range ex.0 - 5 km or 25 km:")
    
    return category,ac_r_not,select_range

auto_15km=Auto('Auto','1 - 15 km',10,'NA','yes')
auto_30km=Auto('Auto','15 - 30 km',8,'NA','yes')
auto_above_30km=Auto('Auto','30 - 500 km',15,'NA','yes')
auto=[auto_15km,auto_30km,auto_above_30km]

micro_15km=Micro('Micro','1 - 15 km',12,14,'yes')
micro_above_15km=Micro('Micro','15 - 300 km',10,12,'yes')
micro=[micro_15km,micro_above_15km]

xl_15km=XL('XL','0 - 15 km',14,15,'yes')
xl_above_15km=XL('XL','15 - 600 km',14,15,'yes')
xl=[xl_15km,xl_above_15km]

goriders=[auto_15km,auto_30km,auto_above_30km,micro_15km,micro_above_15km,xl_15km,xl_above_15km]

(category,ac_r_not,select_range)=(user_selection(auto,micro,xl))
ride=Ride(category,ac_r_not,select_range)
ride.book_ride()
