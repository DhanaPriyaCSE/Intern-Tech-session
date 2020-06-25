
#method1

number=input("Enter the number")
list_num=list(number)
result=reversed(sorted(list_num))
print(''.join(result))

#method2

print(''.join(reversed(sorted(list(input())))))
