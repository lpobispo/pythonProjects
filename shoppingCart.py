# simple shopping cart program with dictionary
# no libraries used
from time import sleep

# dictionary {key}:{value}
menu = {"hamburger": 49.00,
        "pizza": 129.00,
        "popcorn": 29.00,
        "french fries": 39.00,
        "hotdog": 49.00,
        "nuggets": 69.00,
        "cola": 49.00,
        "water": 39.00}

# added method to uppercase the keys in the menu dictionary
upper_dict_menu = {key.upper(): value for key, value in menu.items()}

myCart = []       # added an empty list as the "storage" of the order items
totalAmt = 0      # added a variable for the total amount


print("------------- Menu -------------")

# displayed the dictionary with formatting as a Menu for the users
for key, values in menu.items():
    print(f"     {key:15}: {values:.2f}")

print("--------------------------------")
print()


# Ask input from users for the orders
while True:
    order = input("Type in your order (Press q to quit): ").upper()
    if order == "Q":
        break
    elif upper_dict_menu.get(order) is None:    # Checks if order is within the dictionary(menu)
        print(f"{order} is not available.")
    elif upper_dict_menu.get(order) is not None:
        myCart.append(order)    # add order to myCart list for every correct item in the menu

print("\n------- Your orders are --------\n")


# iterate order through myCart and stores the amount(value) of each to the totalAmt
for order in myCart:
    totalAmt = totalAmt + upper_dict_menu.get(order)
    print(order)

print(f"\nYour total is Php{totalAmt:.2f}\n")   # displays the total amount of users cart

sleep(2)        # 2 seconds delay before the program close