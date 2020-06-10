my_dict = dict()
count_dict_element=int(input("Enter number of key value pair"))
for i in range(count_dict_element):
    user_input = input("Enter key and value separated by commas (,): ")
    key, value = user_input.split(",")
    key=int(key)
    my_dict[key] = value
print(my_dict)
    
swap_dict={value:key for key, value in my_dict.items()}
print(swap_dict)


##Output
'''Enter number of key value pair4
Enter key and value separated by commas (,): 21,FTP
Enter key and value separated by commas (,): 22,SSH
Enter key and value separated by commas (,): 23,telnet
Enter key and value separated by commas (,): 80,http

{21: 'FTP', 22: 'SSH', 23: 'telnet', 80: 'http'}

{'FTP': 21, 'SSH': 22, 'telnet': 23, 'http': 80}'''
