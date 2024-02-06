
print("""
    ______________WELCOME TO ROYAL KITCHEN WARES SHOP___________
""")
salesrep = input("Are you here to buy your kitchen accessories? ")
if salesrep.strip().lower() == "yes":
    print("You're at the right store.")
else:
    print("Check the other store.")
    exit()  
    # Exit the program if the user is not interested

print("""
    ______________Here is our price list___________
""")
price_list = [
    ('8pcs Dinner set', 10000),
    ('Candy Microwave', 22000),
    ('Qasa Microwave', 32000),
    ('Akai Microwave', 15000),
    ('Hoffner pot', 12000),
    ('Ultimate pot', 22000),
    ('Magicook', 50000),
    ('Ocean glass cup', 2000),
    ('Deli glass cup', 9000),
    ('SMP glass cup', 10000),
    ('Qasa electric kettle', 20000),
    ('Kinelco electric iron', 10000),
    ('Master Chef vacuum set', 7000),
    ('Egg rack', 20000),
    ('Portable washing machine', 90000),
    ('5kg cylinder', 10000)
]

cart = []  # Initialize an empty cart

while True:
    print("\nPrice List:")
    for index, (item, price) in enumerate(price_list, start=1):
        print(f"{index}. {item}: #{price}")

    choice = input("Enter the number of the item you want to add to your cart (enter 'done' to finish): ")

    if choice.lower() == 'done':
        break

    try:
        choice = int(choice)
        if 1 <= choice <= len(price_list):
            selected_item = price_list[choice - 1]
            cart.append(selected_item)
            print(f"Item added to your cart: {selected_item[0]}")
        else:
            print("Invalid item number. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Calculate and display the total amount
total_amount = sum(item[1] for item in cart)
print("\nYour Shopping Cart:")
for item, price in cart:
    print(f"{item}: #{price}")

print(f"\nTotal Amount: #{total_amount}")
