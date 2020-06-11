
# pass statement:
""" itis a null operation pass holdes empty body.  """



number=int(input("Enter the number to print no.of times"))

for no_of_iteration in range(1,number):   
    if no_of_iteration==5:
        pass;
        print("pass block")
    print(no_of_iteration)


#output

"""
Enter the number to print no.of times 10
1
2
3
4
pass block
5
6
7
8
9
"""
