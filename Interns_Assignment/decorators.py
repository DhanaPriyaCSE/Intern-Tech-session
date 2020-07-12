
def Outer_function(arg):
    def outer():
        print("Outer\t")
        arg()
        print("Outer\t")
    return outer
    

def Inner_function(arg):
    def inner():
        print("inner\t")
        arg()
        print("inner\t")
    return inner


@Outer_function
@Inner_function
def actual_function():
        print ("inside\t")
actual_function()
