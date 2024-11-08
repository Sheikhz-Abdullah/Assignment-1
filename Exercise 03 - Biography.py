# Step 1: Declear variables for Name & Hometown, then prompt the user to input their details

name = input("Enter your full name: ")
hometown = input("Enter your hometown: ")

# Step 2: Declare a variable for age and the input should be an integer

while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:     # Using ValueError so that the correct input is an integer
        print("Please enter a valid age.")

# Step 3: Make a dictionary to store all the information

user_info = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Step 4: Command to print the user_info

print(f'{user_info["name"]}\n{user_info["hometown"]}\n{user_info["age"]}')  # Using \n to write it in the next line