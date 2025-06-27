#code for gcd 
def gcd(x,y):
    gcd=1
    #used conditional
    if x%y==0:
        return y 
    for k in range(int(y/2),0,-1):
        if x%k==0 and y%k==0:
            gcd =k
            break
        return gcd
print(gcd(12,15))
print(gcd(4,6))
