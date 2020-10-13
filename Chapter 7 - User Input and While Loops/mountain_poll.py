# using while loops with dictionaries
# starting with a blank dictionary that user input will add to.
responses = {}

#setting a flag to indicate polling is active
polling_active = True

while polling_active:
    # Prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the 'responses' dictionary
    # name is the key and response is the value of the key-value pair.
    responses[name.title()] = response.title()

    # find if anyone else is taking the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
