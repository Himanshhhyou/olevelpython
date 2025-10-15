correctAns = {
    "q1": "a",
    "q2": "b",
    "q3": "a",
    "q4": "c",
    "q5": "d",
    "q6": "c",
}
#Dont change anything below
i = 1
marks = 0
while i<=len(correctAns):
    userAns = input(f"Enter option of Q{i}(A/B/C/D): " ).lower()
    key = f"q{i}"
    if userAns == correctAns[key]:
        print("Right")
        marks+=1
    else:
        print("Wrong")
    i+=1
print(f"All check : Your marks is {marks}")

k = 1
while k<=len(correctAns):
    left =f"q{k}"
    right = correctAns[f"q{k}"]
    print(f"{left} - {right}")
    k+=1 #k = k+1
