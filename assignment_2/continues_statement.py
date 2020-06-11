# break statement:
""" it skip the iteration when it reach the condition as true
and continous remainig iterations.
its opposite to break statement """



number=int(input("Enter the number to print no.of times"))

for no_of_iteration in range(1,number):   
    if no_of_iteration==5:
        continue;
    print(no_of_iteration)


#output
#here 5 was skiped.
"""
Enter the number to print no.of times 10
1
2
3
4
6
7
8
9
"""
