num = int(input("Enter the row: ")) 
i = 1
while i <= num:
    print(" "*(num-i), "*"*(2*i-1))
    print("*"*(2*i-1))
    i+=1
