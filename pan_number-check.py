pn = input("Enter your PAN number: ")
#JTRYE9473Q

if len(pn) != 10:
        print("You pan No is invalid")
elif pn[-1].islower():
        print("You pan No is invalid")
else:
    i = 0
    while i<=4:
        if pn[i].islower():
            print("You pan No is invalid")
            break
        i+=1
    else:
       print("Your pan No is valid")