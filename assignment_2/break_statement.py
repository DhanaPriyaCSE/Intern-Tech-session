
# break statement:
""" it terminates the iteration when it reach the condition as true.  """



number=int(input("Enter the number to print no.of times"))

for no_of_iteration in range(1,number):   
    if no_of_iteration==5:
        break;
    print(no_of_iteration)


#output

"""
Enter the number to print no.of times 10
1
2
3
4
"""
