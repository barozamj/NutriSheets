# viewAllMealLogs.py

import json

def view_all_meal_logs():
    #open meal_logs.json if it exists
    try:
        with open("meal_logs.json", "r") as file:
            meal_logs = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Meal history file not found or is empty.")
        return

    # Iterating in reverse order to print newest entries first
    for meal_log in reversed(meal_logs):
        food_items = ', '.join(meal_log['Food Items'].keys())
        print(f"{meal_log['Date']} {meal_log['Time']}, {meal_log['Total Calories']} calories, ${meal_log['Total Cost']:0.2f}, {food_items}")

if __name__ == "__main__":
    view_all_meal_logs()
