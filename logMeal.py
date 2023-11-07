# logMeal.py

import json
from datetime import datetime

# loads all available food items for display to user in log_meal()
def load_food_items():
    try:
        with open("food_items.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Food items file not found. Please register some items first.")
        return None
    
#this function will be called from main.py to log a meal
def log_meal():
    food_items = load_food_items()
    # If no food items are loaded, exit the function
    if food_items is None:
        return

    # initialize dict to hold meal log details
    meal_log = {
        'Date': str(datetime.now().date()),
        'Time': str(datetime.now().time().replace(microsecond=0)), #no microseconds
        'Food Items': {},
        'Total Calories': 0,
        'Total Cost': 0.0
    }

    # loop to allow user to select food items and log them
    while True:
        print("\n0. Press 0 to cancel/go back")
        # display all available food items to the user
        for index, item in enumerate(food_items, start=1):
            print(f"{index}. {item['name']}")
        # input from the user to select a food item
        choice = input("Enter the number of the food item you wish to log or press 0 to cancel/go back: ")
        if choice == '0':
            break   # Exit the loop if the user wishes to cancel
        
        # attempt to parse the selected food item and log the grams
        try:
            item_index = int(choice) - 1
            # Check if the selected index is valid
            if 0 <= item_index < len(food_items):
                selected_item = food_items[item_index]
                # Ask the user for the amount in grams to log
                grams = int(input(f"How many grams of {selected_item['name']} will you log? (1 serving is {selected_item['grams_per_serving']} grams) Enter an integer: "))
                # Add the logged item to the meal log
                meal_log['Food Items'][selected_item['name']] = grams
                # Calculate and add to the total calories and cost
                meal_log['Total Calories'] += round((grams / selected_item['grams_per_serving']) * selected_item['calories'])
                meal_log['Total Cost'] += round((grams / selected_item['net_weight']) * selected_item['cost'], 2)
                print(f"Logged {grams} grams of {selected_item['name']}.\n")
            else:
                print("Invalid selection.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        # allow the user to either continue logging items or submit the meal log
        next_action = input("1. Continue logging items for this meal.\n2. Submit meal log.\nEnter your choice as an integer: ")
        if next_action == '2':
            break

    # add the meal log to the meal_logs.json file if any items were logged
    if meal_log['Food Items']:
        # load existing meal logs or initialize an empty list
        try:
            with open("meal_logs.json", "r") as file:
                meal_logs = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            meal_logs = []

        # Append the new meal log to the meal logs list
        meal_logs.append(meal_log)

        # Write the updated meal logs back to the file
        with open("meal_logs.json", "w") as file:
            json.dump(meal_logs, file, indent=4)

        #print result to user
        print("\nMeal logged!")
        print(f"Date: {meal_log['Date']}")
        print(f"Time: {meal_log['Time']}")
        print("Food Items:", ', '.join([f"{item}: {grams} grams" for item, grams in meal_log['Food Items'].items()]))
        print(f"Total Calories: {meal_log['Total Calories']}")
        print(f"Total Cost: ${meal_log['Total Cost']:0.2f}")
    else:
        print("No items logged.")

if __name__ == "__main__":
    log_meal()