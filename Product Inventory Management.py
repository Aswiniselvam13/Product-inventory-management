# Product Inventory Management

inventory = {}
while True:
    print("\n1. Add Product")
    print("2. View Inventory")
    print("3. Update Quantity")
    print("4. Remove Product")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter product name: ")
        qty = int(input("Enter quantity: "))
        inventory[name] = qty
        print("Product added successfully!")
    elif choice == "2":
        print("\nInventory List:")
        for product, quantity in inventory.items():
            print(product, ":", quantity)
    elif choice == "3":
        name = input("Enter product name to update: ")
        if name in inventory:
            qty = int(input("Enter new quantity: "))
            inventory[name] = qty
            print("Quantity updated!")
        else:
            print("Product not found!")
    elif choice == "4":
        name = input("Enter product name to remove: ")
        if name in inventory:
            del inventory[name]
            print("Product removed!")
        else:
            print("Product not found!")
    elif choice == "5":
        print("Exiting program...")
        break
else:
        print("Invalid choice!")