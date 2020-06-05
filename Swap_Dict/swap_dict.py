my_Dict = dict()
count_Dict_Element=int(input("Enter number of key value pair"))
for i in range(count_Dict_Element):
    user_input = input("Enter key and value separated by commas (,): ")
    key, value = user_input.split(",")
    key=int(key)
    my_Dict[key] = value
print(my_Dict)
    
swap_Dict={value:key for key, value in my_Dict.items()}
print(swap_Dict)


##Output
'''Enter number of key value pair4
Enter key and value separated by commas (,): 21,FTP
Enter key and value separated by commas (,): 22,SSH
Enter key and value separated by commas (,): 23,telnet
Enter key and value separated by commas (,): 80,http

{21: 'FTP', 22: 'SSH', 23: 'telnet', 80: 'http'}

{'FTP': 21, 'SSH': 22, 'telnet': 23, 'http': 80}'''
