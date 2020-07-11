
### 1.

def function_outside():
    msg="Hi"
    def function_inside():
        nonlocal msg #we change the scope of the variable to access for outer fun
        msg="Hello"
        print(msg)
    function_inside()
    print(msg)
function_outside()     

### 2.
def f(x):
    def g(y):
        #return x output is 5
        return y  #1
    return g
a=5
b=1
h=f(a)
print(h(b))


'''
h variable holds 5 after it assign to x then we passing
b value to h now y it holds 1.. when we try to access y means it prints 1
'''


