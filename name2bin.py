name = input("Enter your name: ")  

for i in name:
    aNum = ord(i)      #chr(97)   ord("a")
    binNum = bin(aNum)
    binNum = str(binNum)
    print(binNum[2:], end="")





