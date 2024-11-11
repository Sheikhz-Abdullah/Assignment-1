# Step 1: Create a dictionary where the keys are month numbers and the values are the number of days in those months.

month_days = {
    1: 31,  # January
    2: 28,  # Febuary
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31, # December
}

# Step 2: Create an input where the user will input the month number

month = int(input("Enter the month (1-12): "))

# Step 3: Check if the input is correct

if 1 <= month <= 12:
    if month == 2:       # Check if the month is Febuary and if it's a leap year
        leapyear = input("Is it a leap year? (yes/no): ").strip().lower()
        if leapyear == "yes":
            print("The number of days in February during a leap year is 29.") # If yes then print the year have 29 days
        else:
            print("The number of days in February is 28.")  # If not then print 28 days
    else:
        print(f"The number of days in month {month} is {month_days[month]}.")
else:
    print("Invalid month number! Please enter a number between 1 and 12.") # If the input from user is not an integer then print wrong