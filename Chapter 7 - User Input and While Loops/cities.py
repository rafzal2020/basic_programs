prompt = "\nPlease enter the name of the city you visited: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    # a while True statement will keep a program running permanently
    # while True statements will stop looping when it reaches a break statement.
    city = input(prompt)

    if city == 'quit':
        # the break statement quits a while loop regardless of anything.
        break
    else:
        print(f"I'd love to go to {city.title()}.")

