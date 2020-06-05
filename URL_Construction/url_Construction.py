
#type 1:
#Constructing url using join concept

url_Tuple=('www','Hackerrank','com','domains','python')

url_Tuple_First_Part= ".".join(url_Tuple[:3])
url_Tuple_Second_Part= "/".join(url_Tuple[3:])

print(url_Tuple_First_Part+'/'+url_Tuple_Second_Part)

#type 2
#Constructing url using list concept

url_Tuple=list(tuple(input("Enter the tuple").split()))
url_List=[]
concate='.'.join(url_Tuple[:3]);
url_List.append(concate);
concate='/'.join(url_Tuple[3:])
url_List.append(concate);

converted_To_Tuple=tuple(url_List)
print(converted_To_Tuple[0]+'/'+converted_To_Tuple[1])
