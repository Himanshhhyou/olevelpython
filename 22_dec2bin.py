num = int(input("Enter the number: "))

binaryNum = ""

while num>0:
    lastDigit = num%2 #1
    binaryNum = str(lastDigit)+binaryNum  # 
    num = num//2
print(binaryNum)

