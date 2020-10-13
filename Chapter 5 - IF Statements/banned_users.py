banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
# a list is created of banned users as well as a variable storing the unbanned user.

if user not in banned_users:
	# the keyword 'not' can be used to find items that are NOT included in a list
	# the keyword 'in' can be used to find items that are included in a list. 
	# if 'marie' is not in the 'banned_users' list, print the following: 
		print(f"{user.title()}, you can post a response.")