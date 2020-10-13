players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# the [0:3] means that it will only print the first 3 items in the list. This is called slicing.

print(players[0:5:2])
# adding the 2 at the end makes it so that it will skip through the list by 2. This value can be adjusted to skip greater values in the list. 

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
	# doing ":3" without the first index will print the first item in the list all the way up to the limit of the second index. This works vice versa.
	#using a loop through a slice. 
	print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
# using a variable named "friend_foods" we stored the same list as "my_foods". Using the "[:]" is a good way to copy a list. 

my_foods.append('cannoli')
friend_foods.append('ice cream')
#appending these items to the list is used to prove that these are two completely different lists.

print("My favorite foods are:")
for food in my_foods:
	print(food)

print("\nMy friend's favorite foods are the same:")
for food in friend_foods:
	print(food)


