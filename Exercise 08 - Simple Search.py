# Step 1: Create a list to enter the names

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Step 2: Ask the user for a search word if none is provided, "Sam" will be used by default

search_name = input("Enter the name you want to search for (default is Sam): ") or "Sam"

# Step 3: Search the name in the list

if search_name in names:
    print(f"{search_name} was found in the list.")  # Print if the name was found
else:
    print(f"{search_name} was not found in the list.") # Print if the name was not found