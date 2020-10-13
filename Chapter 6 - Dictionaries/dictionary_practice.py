person = {
	'first_name': 'rayaan', 
	'last_name': 'afzal', 
	'age': 16,
	'city': 'manalapan',
	'school': 'manalapan high school'
	}

person_1 = {
	'first_name': 'pablo',
	'last_name': 'escobar',
	'age': 56,
	'city': 'medellin'
}

person_2 = {
	'first_name': 'adolf',
	'last_name': 'hitler',
	'age': 43,
	'city': 'berlin'
}

persons = [person, person_1, person_2]

for peoples in persons:
	print(peoples)

for info, rayaan in person.items():
	print(f"{info}: {rayaan}")

favorite_numbers = {
	'pablo': 2,
	'rayaan': 5,
	'ash': 17,
	'zach': 92,
	'gunna': 200
	}

for name, numbers in favorite_numbers.items():
	print(f"{name.title()}'s favorite number is {numbers}")

glossary = {
	'append()': 'adds an item to a list',
	'for loop': 'loops through a given list instead of writing a line of code for each item of the list',
	'if': 'a statement that if conditions are met, a line of code will be executed',
	'title()': 'method that capitalizes the first letter of each word',
	'tuple': 'a list that cannot be changed'
	}

glossary['variable'] = 'Used to store a value'
glossary['del'] = 'deletes a key-value pair from a dictionary'
glossary['slicing'] = 'slicing refers to slicing a list at any point in the list'
glossary['pop()'] = 'a method that removes an item from a list but that item is not gone permanently'
glossary['min/max/sum'] = 'functions that allow you to find the minimum/maximum/sum of numbers in a list'

for terms, definitions in glossary.items():
	print(f"Term: {terms} \nDefinition: {definitions}")


