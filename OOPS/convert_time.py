def second(time):
    hour = time // 60
    time %= 60
    minutes = time 
    print("h:m:-> %d:%d" % (hour, minutes))

def mini(hour,m):
    hour=hour*60
    m=m+hour
    return m
def add(a_min,b_min):
    return (a_min+b_min)
def sub(a_min,b_min):
    return abs(a_min-b_min)


a=input("Enter the time").split()
b=input("Enter the time").split()

a_min=mini(int(a[0]),int(a[3]))
b_min=mini(int(b[0]),int(b[3]))
add=add(a_min,b_min)

second(add)
sub=sub(a_min,b_min)
second(sub)
print(add)







