mob_num = input("Enter your mobile number: ")

if (mob_num[0:3] == "+91"):
    if (len(mob_num)==13):
        print("Indian Mobile Number")
    else:
        print("Invalid Mobile Number")
else:
    print("International Mobile Number")