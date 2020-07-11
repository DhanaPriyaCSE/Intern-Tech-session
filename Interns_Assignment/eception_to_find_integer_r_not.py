while True:
    try:
        value = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Enter the input again as integer?")
print("you successfully entered an integer!")

#### OUTPUT
'''
Please enter an integer: yuy
Enter the input again as integer
Please enter an integer: 8.89
Enter the input again as integer
Please enter an integer: g7
Enter the input again as integer
Please enter an integer: 78
you successfully entered an integer!
'''
