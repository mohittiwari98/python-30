#code for gcd 
def gcd(x,y):
    gcd=1
    #used conditional statement
    if x%y==0:
        return y 
        #used for loop
    for k in range(int(y/2),0,-1):
        
        if x%k==0 and y%k==0:
            gcd =k
            break
        return gcd
     
print(gcd(12,15))
print(gcd(4,6))




