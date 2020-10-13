#nesting a dictonary inside a dictionary
users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton'
		},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
		},
	}

# using the dictionary of dictionaries, we created a for loop.
for username, user_info in users.items():
	# one variable name is username for the keys
	# values variable is user_info
	print(f"\nUsername: {username}")
	# prints the key of the key-value pair for each user. 
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']
	# two variables that define the location and names of the users

	# variable are used to print the names and locations
	print(f"\tFull Name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")

