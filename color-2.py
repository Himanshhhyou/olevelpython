colors = set()

choice = "y"
while choice == "y":
    user_input = input("Enter the name of color: ")
    colors.add(user_input)
    choice = input("Want to add more:(y/n): ")
print(colors)
