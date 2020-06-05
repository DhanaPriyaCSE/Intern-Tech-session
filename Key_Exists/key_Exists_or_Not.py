my_Dict = dict()
count_Dict_Element=int(input("Enter number of key value pair"))
for i in range(count_Dict_Element):
    user_input = input("Enter key and value separated by commas (,): ")
    key, value = user_input.split(",")
    my_Dict[key] = int(value)
    print(my_Dict)
    
search_Key=input("Enter the key Element to Search")

#type 1:
for element in my_Dict:
    if element == search_Key:
       print("Key Exits")
    else:
        print("Key doesn't Exits")

#type 2:
if search_Key in my_Dict.keys():
    print("Key Exits")
else:
    print("Key doesn't Exits")

#type 3:
if search_Key in my_Dict:
    print("Key Exits")
else:
    print("Key doesn't Exits")
    

#type 4:python-2 only
'''if my_Dict.has_key(search_Key):
    print("Key Exits")
else:
    print("Key Not Exits")'''


#type 5:
try:
   key= my_Dict[search_Key]
   print("Key Exits")
except:
   print("Key doesn't Exits")

