usernames = []

if usernames:
	for username in usernames:
		if username == 'admin':
			print("Greetings, Admin, need a status report?")
		elif username:
			print(f"Hello, {username.title()}, welcome back.")
else:
	print("We need more people in here!")

current_users = ['rayaan', 'sarah', 'selina', 'pablo', 'travis']
case_sensitive = ['RAYAAN', 'SARAH', 'SELINA', 'PABLO', 'TRAVIS']
new_users = ['TRAVIS','SARAH','heidi','brad','milboer']

for new_user in new_users:
	if new_user in current_users:
		print(f"{new_user.title()} is taken. Please try another name.")
	elif new_user in case_sensitive:
		print(f"{new_user.upper()} is taken. Please try another name.")
	else:
		print(f"{new_user.title()} has successfully created a new user!")

		current_users.append(new_user)
		print(current_users)
		



numbers = list(range(1,10))

for number in numbers:
	if number == 1:
		print(f"{number}st")
	elif number == 2:
		print(f"{number}nd")
	elif number == 3:
		print(f"{number}rd")
	else:
		print(f"{number}th")