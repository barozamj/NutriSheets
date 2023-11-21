import sys
import json
from datetime import date # used for easy calculation of num days in between two given dates (deals with leap years)

def view_calendar_summary(start_date_str, end_date_str):
    """
    Calculate and return the average daily calories consumed and the average daily food spending 
    for a specified time period.

    This function iterates through meal logs within the inclusive date range specified by start_date 
    and end_date. It computes the average daily calories consumed and the average daily cost of food 
    within this time frame. 

    The function expects the meal log data to be available in a format that it can process, 
    and the logic for accessing and iterating through these logs should be implemented within this function.

    Parameters:
    - start_date (str): A string representing the starting date of the period to analyze, in YYYY-MM-DD format.
    - end_date (str): A string representing the ending date of the period to analyze, in YYYY-MM-DD format.

    Returns:
    - str: A JSON-formatted string containing two key-value pairs: 'average_daily_calories' (float) 
           and 'average_daily_cost' (float). These represent the calculated average daily calories 
           consumed and the average daily food spending, respectively.

    Note: The function currently returns placeholder values (0.0 for calories and 0.0 for cost). The actual logic 
    for calculating these averages needs to be implemented within the function.
    """

    # get the date numbers in string form: [YYYY, MM, DD]
    start_date_arr = start_date_str.split('-')
    end_date_arr = end_date_str.split('-')

    # convert strings to integers
    for index in range(3): # 3 represents the three aspects of a date, YYYY, MM, and DD
        start_date_arr[index] = int(start_date_arr[index]) # replace string nums with integer nums
        end_date_arr[index] = int(end_date_arr[index])

    # create date objects to find the difference in days
    start_date = date(start_date_arr[0], start_date_arr[1], start_date_arr[2])
    end_date = date(end_date_arr[0], end_date_arr[1], end_date_arr[2])

    # find the difference in days: note python includes one date and excludes the other
    # ex:
    # for this project, we want the number of days between 2023-01-01 and 2023-01-01 to be 1, but python calculates this to be 0
    # when calling the difference, we need to add one to get the real difference for this project
    difference = end_date - start_date
    total_days = difference.days + 1

    total_calories_consumed = 0.0
    total_spending = 0.0

    # assuming meal_logs.json is in order from least->most recent reading top->bottom
    # find the first meal_log date equal to or later than start_date
    with open("meal_logs.json") as file:
        data = json.load(file)
    
    #####
    # Here, you will add the code to iterate through the appropriate meal logs in [start_date, end_date] inclusive, 
    # and get the average daily calories consumed and average daily food spending for the time period
    # we won't need to worry about a pipeline.json since subprocess communicates between files through stdin/stdout/stderr on the CLI
    # the skeleton code for that has been taken car of below
    # #####

    # go through every entry in the meal log
    for i in range(0, len(data)):
        log_date = data[i]["Date"] # YYYY-MM-DD
        #convert date string into a date object
        log_date = log_date.split('-') # isolate important numbers; [YYYY, MM, DD]
        log_date = date(int(log_date[0]), int(log_date[1]), int(log_date[2])) # create a date object

        if (log_date > end_date): # current date has gone out of bounds (specifically too late)
            break

        # if the current day is in bounds (specifically not too early)
        if (log_date >= start_date):
            # add all the information here
            total_calories_consumed += data[i]["Total Calories"]
            data[i]["Total Cost"]
            total_spending += data[i]["Total Cost"]

    average_daily_calories = total_calories_consumed / total_days
    average_daily_cost = total_spending / total_days
    # return a JSON string
    return json.dumps({
        "average_daily_calories": average_daily_calories,
        "average_daily_cost": average_daily_cost
    })

if __name__ == "__main__":
    if len(sys.argv) == 3:
        start_date = sys.argv[1]
        end_date = sys.argv[2]
        result = view_calendar_summary(start_date, end_date)
        print(result)  # print the result so the main script can capture it
    else:
        print("Invalid number of arguments. Please provide start and end dates.")
