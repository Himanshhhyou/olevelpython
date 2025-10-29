numOfItems = int(input("How many different items you want to buy: "))
items = []
qtys = []
prices=[]

for i in range(1,numOfItems+1):
    print(f"Enter Item {i} detail")
    itemName = input("Item Name: ").lower()
    items.append(itemName)
    qty =  float(input("Enter Qty: "))
    qtys.append(qty)
    price =  float(input("Enter price: "))
    prices.append(price)
    print("======Added successfully======")
##################################
print("Item    Qty    Price    Total")
print("-"*30)

for k in range(0, len(items)):
    i = items[k]
    q = qtys[k]
    p = prices[k]
    print(f"{i}    {q}    {p}    {q*p}")
print("*"*30)
print(f"Grand total: {sum(prices)}")
