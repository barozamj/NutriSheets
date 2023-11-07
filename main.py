#main.py
#Author: Jose Baroza-Martinez
import subprocess

######SUBPROCESSES#############
def register_food_item():
    # call registerFoodItem.py using python subprocess
    subprocess.run(["python", "registerFoodItem.py"], check=True)

def view_food_items():
    # call viewFoodItems.py using python subprocess
    subprocess.run(["python", "viewFoodItems.py"], check=True)

def log_meal():
    # call logMeal.py using python subprocess
    subprocess.run(["python", "logMeal.py"], check=True)

def view_meal_history():
    # call viewMealHistory.py using python subprocess
    subprocess.run(["python", "viewMealHistory.py"], check=True)

def main_menu():
    print("\nWelcome to NutriSheets!")
    print("This program will allow you to register food items, log meals, and view your meal history and nutritional intake.")
    print("If you are a new user, you will need to register a food item before you can log a meal with that food item.")

    while True:  # This loop will continue until the user decides to quit
        print("\nEnter a number to go to:")
        print("1. Register Food Item")
        print("2. View Food Items")
        print("3. Log a Meal")
        print("4. View Meal History")
        print("5. Quit Program")

        choice = input("Please choose an option (1-5): ")
        
        if choice == '1':
            print("You've chosen to register a new food item.\n")
            register_food_item()
        elif choice == '2':
            print("You've chosen to view registered food items.\n")
            view_food_items()
        elif choice == '3':
            print("You've chosen to log a meal.")
            log_meal()
        elif choice == '4':
            print("You've chosen to view meal history.")
            view_meal_history()
        elif choice == '5':
            print("Exiting NutriSheets. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main_menu()
