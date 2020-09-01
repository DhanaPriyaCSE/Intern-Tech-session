noofpairs=int(input("Enter the number of Pairs"));
pairs=list(input("Enter the pairs"));


for pair in len(pairs):
    if(count(pair)==2):
      print("True");
      if(pairs[pair]==pairs[pair+1]):
        print("False")
      
      else:
        print("True")
    
    else:
       print("False");
