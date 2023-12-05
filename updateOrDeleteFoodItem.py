import json

def display_food_items():
    with open('food_items.json', 'r') as file:
        food_items = json.load(file)
        for i, item in enumerate(food_items, 1):
            print(f"{i}. {item['name']}")
        return food_items

def main():
    food_items = display_food_items()
    choice = input("Enter the number of the food item to update/delete (or 0 to go back): ")

    if choice.isdigit() and 0 <= int(choice) <= len(food_items):
        choice = int(choice)
        if choice == 0:
            return
        
        choice -= 1  # Adjust for zero-based indexing

        print("0. Cancel and Return to Main Page")
        print("1. Update Food Item")
        print("2. Delete Food Item")
        action = input("Enter a number to represent an action: ")

        if action == '1':
            update_food_item(food_items, choice)
        elif action == '2':
            delete_food_item(food_items, choice)

def update_food_item(food_items, index):
    print("Updating food item:", food_items[index]['name'])
    print("Leave blank to keep current value.")

    for key in food_items[index]:
        if key == 'name':
            continue  # Assuming we don't allow changing the name for simplicity

        new_value = input(f"Enter new {key} (Current: {food_items[index][key]}): ").strip()
        if new_value:
            if key in ['calories', 'grams_per_serving', 'net_weight', 'cost']:
                food_items[index][key] = type(food_items[index][key])(new_value)
            else:
                food_items[index][key] = new_value

    with open('food_items.json', 'w') as file:
        json.dump(food_items, file, indent=4)

    print("Food item updated successfully.")

def delete_food_item(food_items, index):
    del food_items[index]

    with open('food_items.json', 'w') as file:
        json.dump(food_items, file, indent=4)

    print("Food item deleted successfully.")


if __name__ == "__main__":
    main()
