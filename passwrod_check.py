password = input("Enter your password: ")
if len(password)<8:
    print("Please enter 8 digit or more")
elif ("@" in password) or ("#" in password) or ("$" in password):
    print("Good Password")
else:
    print("Poor Password")
