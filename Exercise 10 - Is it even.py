# Step 1: Determine if the number is even or odd

def check_even_odd(number):
    return f"{number} is even." if number % 2 == 0 else f"{number} is odd."

# Step 2: Ask the user to enetr the number

def main():
    user_input = int(input("Enter a number: ")) 
    print(check_even_odd(user_input))  # Give the function the number and call it

# Step 3: If the script is run directly, run the main function.

if __name__ == "__main__":
    main()