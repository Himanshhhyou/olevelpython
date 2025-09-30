num = int(input("Enter Your number :"))
temp = num
total = 0
while temp>0:
    ld = temp%10
    total = total+(ld**len(str(num)))
    temp //= 10

if num==total:
    print(f"{num} is a Armstrong Number")
else:
    print(f"{num} not a Armstrong Number")
