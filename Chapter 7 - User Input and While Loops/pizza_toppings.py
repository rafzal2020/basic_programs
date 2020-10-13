prompt = "\nWhat toppings would you like on your pizza? "
prompt += "\nEnter 'quit' to exit. "

message = ""
active = True
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(f"Adding {message} to your pizza...")
    else:
        active = False
