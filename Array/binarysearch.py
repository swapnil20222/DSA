# binary search 
def binary(list,n):

    l=0
    u=len(list)-1

    while l<=u:
        mid=(l+u)//2

        if list[mid]==n:
            globals()['pos']= mid
            return True
        else:
            if list[mid]<n:
                l=mid;
            else:
                u=mid;


list=[3123,41414,34234242,123123333,414234324,2342424242342]
n=41414

if binary(list,n):
    print("found",pos+1)
else:
    print("not found")
            
            
