#code for Lcm
#using function with parameters 
def lcm(x,y)::
    if x>y:
        z=x
    else:
        z=y 
    while(True):
        #using while loop
        if((z % x ==0) and (z%y==0)):
            lcm=z
            break
        z+=1
    return lcm
