import random

com_num = random.randint(1,10)
user_num = int(input("Enter any number (1-10): "))

while com_num != user_num:
    print("Not Matched, Try again")
    user_num = int(input("Enter any number (1-10): "))
print(f"You enter {user_num} and computer generate {com_num}")
print("So you WIN")
