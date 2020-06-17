
no_of_rows = int(input("Enter odd number of row "))

if no_of_rows%2!=0:
    for iter_val in range (0, no_of_rows):
        if iter_val %2!=0:
            for inner_val in range(0, iter_val ):
                print("*", end=' ')
            print("\r")
            
    for iter_val  in range (no_of_rows, 0,-1):
        if iter_val %2!=0:
            for inner_val in range(0, iter_val ):
                print("*", end=' ')
            print("\r")
else:
    print("Enter the valid input in odd numbers")
        
#output1
"""
Enter number of rows 5
* 

* * * 

* * * * * 

* * * 

*
"""

#output 2
"""
Enter number of rows 11
* 

* * * 

* * * * * 

* * * * * * * 

* * * * * * * * * 

* * * * * * * * * * * 

* * * * * * * * * 

* * * * * * * 

* * * * * 

* * * 

* 

"""


