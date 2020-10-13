# user inputs and how to use them
# note: sublime text does not work with inputs 
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
# the += operator is used to combine two variables of the same name

message = ""
# a blank message where the user input will be stored.

active = True
# this is called a flag. It is used to keep a program running until something makes the flag untrue.

while message != 'quit':
    # != operator means not equal to.
    # a while loop is used to make it possible to quit the program using user input
    message = input(prompt)

    if message == 'quit':
        active = False
        # when the user inputs 'quit' the flag changes to false ending the program. 
    else:
        print(message)

# the input function allows user input in your program
