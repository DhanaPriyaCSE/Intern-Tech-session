
f=open("priya.txt",'w+')
f=open("priya.txt",'w')
f.write("This is me Dhanapriya.\nI was born in 25-jan-1999 in Trichy\n")
f.close()


f=open("priya.txt",'a')
f.write("Im pursing Bachelor Degree in the stream of Computer Science. ")
f.close()

f=open("priya.txt",'r')
print (f.read())
f.close()
