
#type 1
user_List=list(map(int,input("Enter the Elemnets:").split()))
element_To_Get_Position=int(input("Enter the element to get positions:"))

positions=[]

for elements in range(len(user_List)):
    if user_List[elements]==element_To_Get_Position:
        positions.append(elements)
print(positions)

#prints positions [0, 4, 5, 7]

#type2
#List Compherehence

positions=[elements for elements in range(len(user_List)) if user_List[elements]==element_To_Get_Position]
print(positions)
#prints positions [0, 4, 5, 7]
