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

# function to log a custom food item
def log_custom_food_item(meal_log):
    name = input("Enter Food Item name: ")
    calories = int(input("Enter calories per serving: "))
    grams = int(input("Enter grams of the food item you will log: "))
    cost = float(input("Enter cost of the food item: "))

    # Add the custom food item to the meal log
    meal_log['Food Items'][name] = grams
    meal_log['Total Calories'] += calories
    meal_log['Total Cost'] += cost

# this function will be called from main.py to log a meal
def log_meal():
    food_items = load_food_items()
    # if no food items are loaded, return
    if food_items is None:
        return

    # initialize dict to hold meal log details
    meal_log = {
        'Date': str(datetime.now().date()),
        'Time': str(datetime.now().time().replace(microsecond=0)),
        'Food Items': {},
        'Total Calories': 0,
        'Total Cost': 0.0
    }

    # loop to allow user to select food items and log them
    while True:
        print("\n0. Press 0 to cancel/return to main menu")
        for index, item in enumerate(food_items, start=1):
            print(f"{index}. {item['name']}")
        print(f"{len(food_items) + 1}. Enter a custom food item")

        choice = input("Choose a food item to log or enter a custom item: ")
        if choice == '0':
            break

        #select item and enter amount, then add to total
        try:
            item_index = int(choice) - 1
            if 0 <= item_index < len(food_items):
                selected_item = food_items[item_index]
                grams = int(input(f"How many grams of {selected_item['name']} will you log? Enter an integer: "))
                meal_log['Food Items'][selected_item['name']] = grams
                meal_log['Total Calories'] += round((grams / selected_item['grams_per_serving']) * selected_item['calories'])
                meal_log['Total Cost'] += round((grams / selected_item['net_weight']) * selected_item['cost'], 2)
            elif item_index == len(food_items):  # custom food item entry
                log_custom_food_item(meal_log)
            else:
                print("Invalid selection.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # prompt user if they would like to keep logging or submit meal log
        next_action = input("0. Cancel and return to main menu.\n"
                            "1. Continue logging items.\n"
                            "2. Submit meal log.\n"
                            "Enter your choice: ")
        if next_action == '2':
            break
        elif next_action == '0':
            return  # return to main menu without logging any item

    # only if open the json file if there is something to log
    if meal_log['Food Items']:
        try:
            with open("meal_logs.json", "r") as file:
                meal_logs = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            meal_logs = []

        #add users meal log
        meal_logs.append(meal_log)
        with open("meal_logs.json", "w") as file:
            json.dump(meal_logs, file, indent=4)

        #show th user what they have inputted as meal log
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
