string,anagram=input("enter the string to find anagram or not").split()
string=sorted(string)
anagram=sorted(anagram)
if string==anagram:
    print("True")
else:
    print("False")







