# viewFoodItems.py

import json

#function to display all registered food items
def view_food_items():
    try:
        # Try to open the food_items.json file and load its contents
        with open("food_items.json", "r") as file:
            food_items = json.load(file)
    except FileNotFoundError:
        # If the file does not exist, inform the user
        print("No food items found. Please register some items first.")
        return

    # Print a list of all food items
    print("0. Enter 0 to go back")
    for index, item in enumerate(food_items, start=1):
        print(f"{index}. {item['name']}")

    print("Enter the number of the specified food item to display all information.\nOtherwise, enter 0 to go back.")
    
    # Loop to handle user input
    while True:
        try:
            choice = int(input())   # Get the user's choice as an integer
            if choice == 0:
                break           # If the user chooses 0, exit the function
            elif 1 <= choice <= len(food_items):
                # If a valid item number is chosen, display its details
                selected_item = food_items[choice - 1]
                for key, value in selected_item.items():
                    # Print each detail of the food item
                    print(f"{key.capitalize()}: {value}")
                break
            # If the choice is not within the range, prompt again
            else:
                print("Invalid choice. Please enter a number between 0 and", len(food_items))
        # If the input is not an integer, inform the user
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    view_food_items()
