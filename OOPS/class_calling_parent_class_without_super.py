class Basic:
    x=20
    y=10
    def __init__(self):
        pass
    def addition(self):
        return Basic.x + Basic.y
    
    def subtraction(self):
        return Basic.x - Basic.y

    def time_table(self):
        for i in range(1,Basic.y):
            print("%i * %i = %i" %(i,Basic.y,(i * Basic.y)))



class Advanced(Basic):
    x=5
    y=5
    def __init__(self):
        pass

    def power(self):
        print( self.x ** self.y)

    def time_advanced(self):
        for i in range(1,self.y):
            print("%i * %i = %i" %(i,self.y,(i * self.y)))


class Composition:
    def __init__(self):
        #self.base=Basic()
        self.base=Advanced()

    def comp_power(self):
        return self.base.power()

    def multiply(self):
        print(self.base.x * self.base.y)

    def time_y(self):
        return self.base.time_table()
    
b = Basic()
#b.time_table()

a= Advanced()
a.time_table()
a.time_advanced()

c=Composition()
c.multiply()
#c.time_y()
c.comp_power()
c.base.time_table()
c.base.time_advanced()





                  
