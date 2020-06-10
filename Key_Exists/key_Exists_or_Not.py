my_dict = dict()
count_dict_element=int(input("Enter number of key value pair"))
for i in range(count_dict_element):
    user_input = input("Enter key and value separated by commas (,): ")
    key, value = user_input.split(",")
    my_dict[key] = int(value)
    print(my_dict)
    
search_key=input("Enter the key Element to Search")

#type 1:
for element in my_dict:
    if element == search_key:
       print("Key Exits")
    else:
        print("Key doesn't Exits")

#type 2:
if search_key in my_dict.keys():
    print("Key Exits")
else:
    print("Key doesn't Exits")

#type 3:
if search_key in my_dict:
    print("Key Exits")
else:
    print("Key doesn't Exits")
    

#type 4:python-2 only
'''if my_dict.has_key(search_key):
    print("Key Exits")
else:
    print("Key Not Exits")'''


#type 5:
try:
   key= my_dict[search_key]
   print("Key Exits")
except:
   print("Key doesn't Exits")

