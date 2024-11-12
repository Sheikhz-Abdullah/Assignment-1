# Step 1: Create variables to define the password and the amount of attempts the user have

right_password = 12345
max_attempts = 5
attempts = 0

# Step 2: Use a while loop to limit the attempts

while attempts < max_attempts:

    try:
# Step 3: Ask the user for the password

        user_password = int(input("Enter the password: "))  # User need to enter the password

        if user_password == right_password:
            print("Password accepted! You have gained access.")
            break
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            if remaining_attempts > 0:
                print(f"Incorrect password. You have {remaining_attempts} attempt(s) left.")
            else:
                print("Maximum attempts reached. The authorities have been alerted.")

    except ValueError:
        print("The value entered is not correct! Enter a number.")