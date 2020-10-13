name = "ada lovelace"
print(name.title())
#title() method changes first letter of each word to uppercase
#The "." after name in name.title is used to tell python
#to use the title method for the code. 

#"()" is used to store needed information for the method

print(name.upper())
#upper() method changes the variable to uppercase

print(name.lower())
#lower() method changes the variable to lowercase

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
#the letter f in this line of code stands for format. It is known as an f string
#Placing the f before connecting the two strings together tells python to format the string by replacing the variable name with its value.
 
print(f"Hello, {full_name.title()}!")
#You can create implement variables of strings into a full message as shown in the line of code above.

message = f"Hello, {full_name.title()}!"
print(message)
#You can use f strings to create a message and store that message in a variable as shown above. 

###WHITESPACE###

print("\tPython")
#\t is a type of whitespace which tabs the text. 

print("Languages: \nPython\nJava\nC")
#\n is another whitespace which creates a new line for each piece of text that has \n written before it.

print("Languages: \n\tPython\n\tJave\n\tC")
#You can combine two white spaces. This one in particular makes it so each new text is indentented and put on a new line. 

favorite_language = ' python '
#Notice the space before and after python in the variable
print(favorite_language.rstrip())
#the .rstrip() method eliminates the white space or the space to the right of ' python '. 

print(favorite_language.lstrip())
#the .lstrip() method elimnates white space on the left of ' python '

print(favorite_language.strip())
#the .strip() eliminates both sides of white space in ' python '

