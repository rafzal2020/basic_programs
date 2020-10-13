prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "
# we could add two messages in for one variable and print those two messages at the same time.

name = input(prompt)
# a variable is created that stores an input function value asking for your name.
print(f"\nHello, {name}")
