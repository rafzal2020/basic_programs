# store a list in a dictionary with this example
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese']
	# we put a list for toppings as shown above within the dictionary.
}

print(f"You order a {pizza['crust']}-crust pizza. "
	"with the following toppings:")

for topping in pizza['toppings']:
	print(f"\t{topping}")