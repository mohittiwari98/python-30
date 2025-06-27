#find max of three 
#first find max of two
#using function with parameters
def max_of_two(x,y):
    #usimg conditional statements 
    if x>y:
        return x
    return y 
def max_of_three(x,y,z):
    return max_of_two(x,max_of_two(y,z))
print(max_of_three(3,6,7))
