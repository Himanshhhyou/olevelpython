import calendar

#complete year
#print(calendar.calendar(2025))

#specific month
print(calendar.month(2025,10))

#leap year check
print(calendar.isleap(2020))

#0 - mon , 1 tuesday 2- wednesday,..................
d = calendar.weekday(2025,10,12))

if d == 0:
    print("Monday")
elif d == 1:
    print("Tuesday")
elif d == 2:
    print("Wednesday")
elif d == 3:
    print("Thursday")
elif d == 4:
    print("Friday")
elif d == 5:
    print("Saturday")
else:
    print("Sunday")

    print("Invalid day")
