# registerFoodItem.py

def register_food_item():
    name = input("Enter Food Item name: ")
    calories = input("Enter calories per serving: ")
    grams_per_serving = input("Enter grams/serving: ")
    net_weight = input("Enter food item net weight: ")
    cost = input("Enter food item cost: ")

    # Construct the food item data string
    food_item_data = f"{name},{calories},{grams_per_serving},{net_weight},{cost}\n"

    # Write the food item data to a local file
    with open("food_items.csv", "a") as file:
        file.write(food_item_data)

    print("Food item registered successfully!")

if __name__ == "__main__":
    register_food_item()
