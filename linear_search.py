#linear search
#using function
def linearsearch(array,n,x):
    #used for loop
    for i in range(0,n):
        if(array[i]==x):
            return i 
        return -1
#given
array =[1,2,5,4,7,5]
x=1
n=len(array)
result = linearsearch(array,n,x)
if(result == -1):
    print("element not found")
else:
    print("element found at index: ",result)
