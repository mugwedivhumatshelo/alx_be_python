# Initialize an empty shopping list
shopping_list = []

def display_menu():
    """Displays the main menu to the user."""
    print("\nShopping List Manager")
    print("1. Add item to list")
    print("2. Remove item from list")
    print("3. View shopping list")
    print("4. Exit")

def add_item():
    """Prompts the user for an item name and adds it to the shopping list."""
    item_name = input("Enter the item name: ")
    shopping_list.append(item_name)
    print(f"{item_name} added to the shopping list.")

def remove_item():
    """Asks the user for an item name and removes it from the shopping list."""
    item_name = input("Enter the item name to remove: ")
    if item_name in shopping_list:
        shopping_list.remove(item_name)
        print(f"{item_name} removed from the shopping list.")
    else:
        print(f"{item_name} not found in the shopping list.")

def view_list():
    """Prints each item in the shopping list to the console."""
    if shopping_list:
        print("\nShopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    else:
        print("Shopping list is empty.")

def main():
    """Runs the shopping list manager."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            view_list()
        elif choice == "4":
            print("Exiting the shopping list manager.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
