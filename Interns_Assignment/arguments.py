def fun(name,*a):
    total=0
    for i in a:
        total+=(int(i))
    avg=total/len(a)
    print(name+"-"+str(avg))
    
fun("priya",80,96,84,70,56)


# output #

# priya-77.2 #
