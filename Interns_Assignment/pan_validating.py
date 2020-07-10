import re

string=input("Enter the string")

regex='[A-Z]{5}[\d]{4}[A-Z]{1}'

if(re.search(regex,string)):
    print("True")
else:
    print("False")

    
