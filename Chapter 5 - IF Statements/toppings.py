requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
	#the "!=" means not equal.
	#if the requested topping (mushrooms) is not anchovies, then print the following:
	print('Hold the anchovies!')

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese")
# Multiple if statements are used compared to using elif statements.
# if an elif statement was used, it would only print one of the toppings because elif statements only need to pass on test
# a series of simple if statements makes it so your code must pass several tests in order to work. 

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		#this if statement is stating that they are out of green peppers.
		#We are combining for loops and if statements together
		print("We are out of green peppers.")
	else:
		print(f"Adding {requested_topping}.")
	# there are no more green peppers left but will add the other given toppings. 

print("\nFinished making your pizza!")

requested_toppings = []
# empty list which signifies user input did not put any toppings for the pizza

if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}.")
	print("\nFinished making your pizza!")
	# here it is saying that if there were given toppings from the user, it would use this part of the program
else:
	print("Are you sure you want a plain pizza?")
	#There was no toppings in the list so this is printed instead.

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
# making a list of toppings that are allowed and having a user put in random things in their list. 
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"{requested_topping.title()} is not an available topping.")
		#here is shows that french fries is not in the available toppings list and so it will not be added. 