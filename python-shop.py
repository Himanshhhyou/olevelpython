shop = [
    ["apple", 60],
    ["kiwi", 90],
    ["banana", 40]
]
cart, notFound = [], []

while True:
    for item, price in shop:
        print("{} - {}rs./kg".format(item.title(), price))
    print("------------------------")
    wantBuy = input("Would you like to buy something? (y/n): ").lower()
    if wantBuy == "y" or wantBuy == "yes":
        choice = input("What would you like to buy: ")
        for fruit in shop:
            if choice == fruit[0]:
                qty = int(input("Enter the Quantity: "))
                print("____________________")
                cart.append([choice, qty])
                break
        else:
            notFound.append(choice)
            print("********This item is not available********")
            print("____________________")
    elif wantBuy == "n" or wantBuy == "no":
        break
    else:
        print("******Please answer with yes or no**********")
        print("____________________")

if len(notFound) != 0:
    print("\nItems not available in shop: ", notFound)
else:
    print()

total = 0
print("\n----Customer Cart----")
for item, qty in cart:
    for shopItem, price in shop:
        if item == shopItem:
            print("{} x {} = {}Rs.".format(item, qty, qty * price))
            total += qty * price
print("___________________")
print("\nTotal bill: ", total, "Rs")
