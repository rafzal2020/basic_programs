user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi'
}

# looping through a dictionary
for key, value in user_0.items():
	# the 'key' and the 'value' in this for loop are names of variables
	# these variable names can be anything but make it simple and easy to follow
	# the .items() method returns the list of key-value pairs.
	print(f"\nKey: {key}")
	# using the 'key' variable defined earlier, we print the Key part of each key-value pair
	print(f"Value: {value}")
	# using the 'value' variable defined in the for loop, we print the value part of each key-value pair. 