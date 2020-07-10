import re

floating_point_num=input("Enter the number")
regex='^[+-]?([0-9]+)?\.[0-9]+'
if (re.search(regex,floating_point_num)):
    print("True")
else:
    print("False")
