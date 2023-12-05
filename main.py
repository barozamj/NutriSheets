#main.py for NutriSheets project
#Author: Jose Baroza-Martinez

import re
import subprocess
import sys
import json

######SUBPROCESSES#############
def register_food_item():
    # call registerFoodItem.py using python subprocess
    subprocess.run([sys.executable, "registerFoodItem.py"], check=True)

def view_food_items():
    # call viewFoodItems.py using python subprocess
    subprocess.run([sys.executable, "viewFoodItems.py"], check=True)

def log_meal():
    # call logMeal.py using python subprocess
    subprocess.run([sys.executable, "logMeal.py"], check=True)

def view_all_meal_logs():
    # call viewAllMealLogs.py using python subprocess
    subprocess.run([sys.executable, "viewAllMealLogs.py"], check=True)

def update_or_delete_food_item():
    subprocess.run([sys.executable, "updateOrDeleteFoodItem.py"], check=True)

def view_calendar_summary():
    # input validation for YYYY-MM-DD
    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')

    # prompt the user for start and end dates
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")

    # validate date format
    if not date_pattern.match(start_date) or not date_pattern.match(end_date):
        print("Input not in valid YYYY-MM-DD format")
        return  # return to the main page

    # vall viewCalendarSummary.py with the start and end dates as arguments
    result = subprocess.run([sys.executable, "viewCalendarSummary.py", start_date, end_date], capture_output=True, text=True, check=True)
    
    # parse the output from viewCalendarSummary.py
    output = result.stdout.strip()
    data = json.loads(output)  # assuming the output is a JSON string

    # extract average_daily_calories and average_daily_cost
    average_daily_calories = data['average_daily_calories']
    average_daily_cost = data['average_daily_cost']

    # print the results
    print(f"\nFrom {start_date} to {end_date}:")
    print(f"Average daily consumed calories: {round(average_daily_calories)}")
    print(f"Average daily food spending: ${average_daily_cost:.2f}")

def main_menu():
    print("\nWelcome to NutriSheets!")
    print("This program will allow you to register food items, log meals, and view your meal history and nutritional intake.")
    print("If you are a new user, you will need to register a food item before you can log a meal with that food item.")

    while True:  # This loop will continue until the user decides to quit
        print("\nEnter a number to go to:")
        print("1. Register Food Item")
        print("2. View Food Items")
        print("3. Log a Meal")
        print("4. View All Meal Logs")
        print("5. View Calendar Summary")
        print("6. Update or Delete Food Item")
        print("7. Quit Program")

        choice = input("Please choose an option (1-7): ")
        
        if choice == '1':
            print("\nYou've chosen to register a new food item.")
            register_food_item()
        elif choice == '2':
            print("\nYou've chosen to view registered food items.")
            view_food_items()
        elif choice == '3':
            print("\nYou've chosen to log a meal.")
            log_meal()
        elif choice == '4':
            print("\nYou've chosen to view all meal logs.")
            view_all_meal_logs()
        elif choice == '5':
            print("\nYou've chosen to view calendar summary.")
            view_calendar_summary()
        elif choice == '6':
            print("\nYou've chosen to update or delete a registered food item.")
            update_or_delete_food_item()
        elif choice == '7':
            print("\nExiting NutriSheets. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main_menu()
