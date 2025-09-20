#simple interest

#accepting 
p = float(input("Enter the principle ammount: "))
t = float(input("Enter the time period: "))
r = float(input("Enter the rate of interest: "))

#calculate si
si = (p*r*t)/100

#design
print("*"*30)

#printing
print("Your interest is: {} rs.".format(si))
print("Totoal payable ammount: {} rs.".format(p+si))

#design
print("*"*30)
