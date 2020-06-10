
#type 1
user_list=list(map(int,input("Enter the Elemnets:").split()))
element_to_get_position=int(input("Enter the element to get positions:"))

positions=[]

for elements in range(len(user_list)):
    if user_list[elements]==element_to_get_position:
        positions.append(elements)
print(positions)

#prints positions [0, 4, 5, 7]

#type2
#List Compherehence

positions=[elements for elements in range(len(user_list)) if user_list[elements]==element_to_get_position]
print(positions)
#prints positions [0, 4, 5, 7]
