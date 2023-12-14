#registerFoodItem.py

import json

def register_food_item():
    # Prompt for food item details
    name = input("Enter Food Item name: ")
    calories = input("Enter calories per serving (ex. 200): ")
    grams_per_serving = input("Enter grams per serving (ex. 30): ")
    net_weight = input("Enter food item net weight in grams (ex. 907): ")
    cost = input("Enter food item cost in dollars (ex. 4.99): ")

    # Create a dictionary for the food item
    food_item = {
        "name": name,
        "calories": int(calories),  
        "grams_per_serving": float(grams_per_serving),  
        "net_weight": float(net_weight),  
        "cost": float(cost)  
    }

    # read the existing data and update it
    try:
        with open("food_items.json", "r") as file:
            food_items = json.load(file)
    except FileNotFoundError:
        # if the file doesn't exist, start with an empty list
        food_items = []

    # append the new food item
    food_items.append(food_item)

    # write the updated data back to the file
    with open("food_items.json", "w") as file:
        json.dump(food_items, file, indent=4)

    print("Food item registered successfully!")

if __name__ == "__main__":
    register_food_item()
