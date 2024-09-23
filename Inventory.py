def display_inventory(inventory):
    print("Inventory list:")
    for i in inventory:
        print(i,":",inventory[i],end = "\n")

def update_inventory(inventory):
    objt = input("Enter the product name you want to update: ")
    if inventory.get(objt) == None:
        ans = input(objt + " is not in the inventory. Would you like to add it? (y/n): ")
        if ans == 'y':
            inventory[objt] = {}
            n = int(input("Enter the quantity to add: "))
            inventory[objt] = n
            print(f"Added new product Notebook with quantity {inventory[objt]}")
        else:
            return inventory
    else:
        n = int(input("Enter the quantity to add or subtract: "))
        inventory[objt] += n
        if inventory[objt] >= 0:
            print(f"The updated quantity of Laptop is: {inventory[objt]}")
        else:
            print("Cannot reduce the quantity of Phone because it will result in a negative amount!")
            inventory[objt] -= n
        
def delete_inventory(inventory):
    objt = input("Enter the product name you want to delete: ")
    ans = input(f"Are you sure you want to delete {objt}? (y/n): ")
    if ans == 'y':
        print(f"{objt} has been deleted from the inventory.")
        del inventory[objt]
    else:
        return inventory
   
def main():
    bool = True
    inventory = {"Laptop": 10,"Phone": 25,"Tablet": 15}
    while(bool):
        
        print("Inventory Management System:\n1. View inventory list\n2. Add/Reduce products\n3. Delete products\n4. Exit the program")
        op = int(input("Select an option: "))
        print("\n")
        if op == 1:
            display_inventory(inventory)
        elif op == 2:
            update_inventory(inventory)
        elif op == 3:
            delete_inventory(inventory)
        elif op == 4:
            print("Exiting the program")
            bool =False
        print("\n")
main()
       