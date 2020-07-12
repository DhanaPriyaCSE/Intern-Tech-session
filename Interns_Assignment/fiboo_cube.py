

from functools import reduce

fibonacci = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
number=int(input("Enter the number"))
print(fibonacci(number))


### Output
'''
Enter the number 10
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''

cube_num=int(input(("Enter the number")))
cube_nums = lambda x: True if round(x ** (1. / 3)) ** 3 == x else False
print(cube_nums(cube_num))

