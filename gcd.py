num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    minNum = num2
else:
    minNum = num1
i = 2
while i <= minNum:
    if num1%i==0 and num2%i==0:
        gcd = i  #2 4 5 10 20
    i+=1 
print(gcd)