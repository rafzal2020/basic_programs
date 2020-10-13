# listing favorite languages of 4 people in this format
favorite_languages = {
	'jen': 'python',
	'sarah': 'c', 
	'edward': 'ruby', 
	'phil': 'python'
	}

# storing Sarah's favorite language in a variable.
for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")

#making a list of friends that are also in the dictionary favorite_languages
friends = ['phil', 'sarah']
# for loop through a dictionary but only with the keys in the key-value pairs.
for name in favorite_languages.keys():
	# the keys() method is useful when you only need to work with the keys of the key-value pairs. 
	# prints a greeting to a name in the dictionary 
	print(f"Hi, {name.title()}.")

	if name in friends:
		# if the name in 'friends' is also in 'favorite_languages' do this:
		language = favorite_languages[name].title()
		# storing the name from the dictionary in a variable
		print(f"\t{name.title()}, I see you love {language}!")
		# printing the name in the dictionary and what language they love. 

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll")

for name in sorted(favorite_languages.keys()):
	# you can use the sorted() method to sort keys in key-value pairs.
	print(f"{name.title()}, thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	# the set function will look for duplicate items and group them together so that there are no repeating items in the list. 
	# the value() method lists solely the values listed in the key-value pairs
	# in other words, its the opposite of the keys() method. 
	print(language.title())

language_poll = ['phil', 'jen', 'jack', 'don']

for name in favorite_languages.keys():
	if name in language_poll:
		print(f"Thank you for taking the poll, {name.title()}")
	else:
		print(f"Please take the poll.")




