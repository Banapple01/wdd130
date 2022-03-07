"""
File: shopping.py
Author: Jonathan Wright

Purpose: Go shopping.
"""

cart = []
act = ""

while act != 5:
    print('''Please select one of the following:
    1. Add item
    2. View cart
    3. Remove item
    4. Compute total 
    5. Quit''')
    act = int(input("Please enter an action: "))
    if act == 1:
        item_details = []
        item = str(input("What item would you like to add? "))
        price = "{:.2f}".format(float(input(f"What is the price of '{item.title()}'? ")))
        item_details.append(item.capitalize())
        item_details.append(float(price))
        cart.append(item_details)
        print(f"'{item_details[0]}' has been added to the cart.\n")
    elif act == 2:
        if cart.__len__() != 0:
            i = 1
            for item in cart:
                print(f"{i}. {item[0]} - ${item[1]}")
                i+=1
        else:
            print("There are no items in your cart.")
        print("\n")
    elif act == 3:
        if cart.__len__() != 0:
            i = 1
            for item in cart:
                print(f"{i}. {item[0]} - ${item[1]}")
                i+=1
            remove = int(input("Which item would you like to remove? (0 to cancel): "))
            if remove > 0:
                remove -= 1
                try:
                    confirm = cart[remove]
                    cart.remove(cart[remove])
                    print(f"{confirm[0]} - ${confirm[1]} has been removed.\n")
                except:
                    print("There was a problem removing the item. Please ty again.\n")
            else:
                print("canceled\n")
        else:
            print("There are no items in your cart.")
        print("\n")
    elif act == 4:
        if cart.__len__() != 0:
            i = 0
            j=1
            for item in cart:
                print(f"{j}. {item[0].title()} - ${item[1]}")
                j+=1
                i+=item[1]
            i = "{:.2f}".format(i)
            print(f"The total price of the items in the shopping cart is ${i}")
        else:
            print("There are no items in your cart.")
        print("\n")
    else:
        print("Thank you. Goodbye.\n")
