cart = []

while True:
    print("\nShopping Cart Menu")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Checkout")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        item = input("Enter item to add: ")
        cart.append(item)
        print(item, "added to cart.")

    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
            print(item, "removed from cart.")
        else:
            print("Item not in cart.")

    elif choice == "3":
        print("Your cart:", cart)

    elif choice == "4":
        print("Checking out...")
        print("Final cart:", cart)
        break

    else:
        print("Invalid choice.")
