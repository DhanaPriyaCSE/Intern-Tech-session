arr=list(input("Enter the pair of array"))




s=int(input("Enter the sum "))


for i in range(len(arr)):
  total=0
  total+=int(i)
  if total== s:
    count=0
    if(i+(i+1)=s):
      count+=1
      print("The number of pairs is {}".format(count));
    else:
      print("There is no pair")

      