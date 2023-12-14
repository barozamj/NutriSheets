def explain_feature(option):
    explanations = {
        '1': "Register Food Item: This function allows you to register a food item that can be"
            " repeatedly used in the Log a Meal operation. Registering a food item has the benefit of"
            " shortening the process of logging a meal if this is an item you expect to repeatedly log",
        '2': "View Food Items: Displays a list of all registered food items."
            " You can also view additional information about each of the food items that you have entered.",
        '3': "Log a Meal: Lets you record the details of a meal you've had. This operation can work by either entering a pre-registered"
            " food item and the amount in grams that you consumed, or instead by inputting a food item that is not registered. This allows"
            " the benefit of easily inputting something you routinely consume or the versatility of inputting something you do not intend to"
            " input again.",
        '4': "View All Meal Logs: Shows a history of all logged meals. Order is from oldest to most recent.",
        '5': "View Calendar Summary: Provides a summary of meals over a selected period. This summary consists of daily calories consumed over "
            "this period and average daily cost. The user must enter the date in YYYY-MM-DD format.",
        '6': "Update or Delete Food Item: Modify or remove existing registerred food items. You may update the calories per serving, "
            "the grams per serving, the net weight, and the total cost of product. The name is not alterable."
    }

    return explanations.get(option, "Invalid option. Please enter a number between 1 and 6.")

def main():
    while True:
        print("\nEnter the number for which you want an explanation:")
        print("1. Register Food Item")
        print("2. View Food Items")
        print("3. Log a Meal")
        print("4. View All Meal Logs")
        print("5. View Calendar Summary")
        print("6. Update or Delete Food Item")

        print("\n Or enter 0 to return to the main menu.")


        choice = input("\nChoose an option (0-6): ")

        if choice == '0':
            break

        print(explain_feature(choice))

if __name__ == "__main__":
    main()
