

# Predefined fruit price list
fruit_shop = {
    "mango": 30,
    "kiwi": 90,
    "apple": 100,
    "lemon": 30,
    "orange": 50
}

# Lists to store cart details
cart_items = []
quantities = []

# User input loop
repeat = "y"
while repeat == "y":
    item_name = input("\U0001F34A Enter the fruit you want to buy: ").lower()

    if item_name in fruit_shop:
        cart_items.append(item_name)
        item_quantity = int(input(f"\U0001F4E6 Enter quantity of {item_name}: "))
        quantities.append(item_quantity)
        print(f"\u2705 {item_name.title()} added successfully!\n")   # ✅
    else:
        print(f"\u274C Sorry, {item_name} is not available right now.\n")  # ❌

    repeat = input("\U0001F501 Do you want to buy something else? (y/n): ").lower()

# Display cart summary
print("\n\U0001F6D2 Your Cart Summary:")
total_amount = 0
for index in range(len(cart_items)):
    fruit = cart_items[index]
    quantity = quantities[index]
    price = fruit_shop[fruit] * quantity
    total_amount += price
    print(f"\U0001F34F {fruit.title()} × {quantity} = ₹{price}")

print(f"\n\U0001F4B0 Total Amount: ₹{total_amount}")
print("\u2728 ****** Thanks for shopping with us! ****** \u2728")
