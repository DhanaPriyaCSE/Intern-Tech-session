wclass Basic:
    def __init__(self,x=20,y=8):
        self.x=x
        self.y=y
    def addition(self):
        return self.x + self.y
    
    def subtraction(self):
        return self.x - self.y

    def time_table(self):
        for i in range(1,self.y):
            print("%i * %i = %i" %(i,self.y,(i * self.y)))



class Advanced(Basic):
    def __init__(self,x=10,y=8):
        super().__init__(x,y)

    def power(self):
        print( self.x ** self.y)


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
    

'''
b = Basic()
b.time_table()

a= Advanced()
a.multiply()
a.time_table()
'''


c=Composition()
c.multiply()
c.time_y()
c.comp_power()

                  
