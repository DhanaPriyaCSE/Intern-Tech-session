start,end=map(int,input("Enter the range start and end").split())
num1,num2=map(int,input("Enter the 2 divsor ").split())
for val in range(start,end+1):
    if (val%num1==0 and val%num2==0):
        print(val)
print()
        
#output
"""
Enter the range start and end200 1500
Enter the 2 divsor 75 100
300
600
900
1200
1500
"""
