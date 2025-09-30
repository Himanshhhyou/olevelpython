num = int(input("Enter the number: "))
i = 2
while i < num:
    if num%i==0:
        print("Not Prime")
        break
    i+=1
else:
    print("Prime")

        