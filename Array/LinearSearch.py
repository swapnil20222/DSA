#Linear search programme
def linearsearch(list,n):
 i=0

 while i<len(list):
   if list[i]==n:
       return True
   i=i+1
 return False

list=[2,31,42,123,32134,2334,1231]
n=43


if linearsearch(list,n):
    print("Found")
else:
    print("Not found")

