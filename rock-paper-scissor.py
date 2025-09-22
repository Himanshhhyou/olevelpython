import random

while True:
    rNum = random.randint(1,3)
    if rNum == 1:
        com = "rock"
    if rNum == 2:
        com = "paper"
    if rNum ==3: 
        com = "scissor"

    print("Rock , Paper, Scissor")
    user = input("Enter Your choice: ").lower()


    if com == user:
        print("Game Draw")
    elif (user=="rock" and com == "scissor") or \
        (user=="paper" and com=="rock")  or \
        (user == "scissor" and com=="paper"):
        print("="*30)
        print("You win because you choose {} and computer choose {}".format(user,com))
        print("="*30)
    else:
        print("Computer win because you choose {} and computer choose {}".format(user,com))



    



