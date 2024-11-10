# Step 1: Create a dcitionary for the European countries with there capitals

quiz = {
    "France": "Paris",
    "Sweden": "Stockholm",
    "Switzerland": "Bern",
    "Austria": "Vienna",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Belgium": "Brussels",
    "Netherlands": "Amsterdam",
    "Portugal": "Lisbon"
}

# Step 2: Go through every quiz question in turn

for country, capital in quiz.items():
    answer = input(f"What is the capital of {country}?").strip()   #Ask the query and receive the user's response.

# Step 3: Analyze the answer wihtout having the case

    if answer.lower() == capital.lower():
        print(f"Correct! The capital of {country} is {capital}.")
    else:
        print(f"Incorrect! The capital of {country} is {capital}.")