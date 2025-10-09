#linear search

numList = [10, 23, 45, 70, 11, 15, 90, 34]
target = int(input("Enter the num: "))

i = 0
while i < len(numList):
    if numList[i] == target:
        print(f"{target} found at index {i}")
        break
    i=i+1
else:
    print(f"{target} is not in the list")
