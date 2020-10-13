vacation_poll = {}

poll_active = True
while poll_active:
    name = input("\nWhat is your name? ")
    response = input("\nWhere do you want to go for vacation? ")

    vacation_poll[name] = response
    new_response = input("\nWould you like to take the poll again? (yes/no) ")
    if new_response == 'no':
        poll_active = False

print("\n--- The Poll Results ---")
for name, response in vacation_poll.items():
    print(f"{name.title()} wants to go to {response.title()}.")
