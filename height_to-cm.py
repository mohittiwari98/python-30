#height to cm conveter
print("input your height")
h_ft = int(input("feet: "))
h_inch = int(input("inches:"))
h_inch=+ h_ft*12
h_cm = round(h_inch*2.54,1)
print("your height is %d cm" % h_cm)
