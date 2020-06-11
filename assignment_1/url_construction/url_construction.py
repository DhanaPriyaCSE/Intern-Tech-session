
#type 1:
#Constructing url using join concept

url_tuple=('www','Hackerrank','com','domains','python')

url_tuple_first_part= ".".join(url_tuple[:3])
url_tuple_second_part= "/".join(url_tuple[3:])

print(url_tuple_first_part+'/'+url_tuple_second_part)

#type 2
#Constructing url using list concept

url_tuple=list(tuple(input("Enter the tuple").split()))
url_list=[]
concate='.'.join(url_tuple[:3]);
url_list.append(concate);
concate='/'.join(url_tuple[3:])
url_list.append(concate);

converted_to_tuple=tuple(url_list)
print(converted_to_tuple[0]+'/'+converted_to_tuple[1])
