import calendar
y = int(input("Enter Year: "))
m = int(input("Enter month: "))
d = int(input("Enter date: "))

w = calendar.weekday(y,m,d)

if w == 0:
    print("Monday")
elif w == 1:
    print("Tuesday")
elif w == 2:
    print("Wednesday")
elif w == 3:
    print("Thursday")
elif w == 4:
    print("Friday")
elif w == 5:
    print("Saturday")
else:
    print("Sunday")
