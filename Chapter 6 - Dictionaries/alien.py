alien_0 = {'color': 'green', 'points': 5}
#this is a dictionary which allows you to store pieces of related information
#a dictionary is wrapped in {}.

print(alien_0['color'])
print(alien_0['points'])
# this is how to print a value associated with a key in the dictionary

new_points = alien_0['points']
print(f"You just earned {new_points} points!")
# we turned the 'points' valur in the dictionary to a variable then printed that variable in a message.

alien_0['x_position'] = 0
alien_0['y_position'] = 25
# this adds two new key-value pairs to the dictionary 'alien_0'
print(alien_0)

# making a blank dictionary and adding key-value pairs separately
alien_0 = {}

# adding color and point key-values to the alien_0 blank dictionary
alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# modifying values in a dictionary

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original Position: {alien_0['x_position']}")

# move the alien to the right.
# determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# This must be a fast alien
	x_increment = 3

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New Position: {alien_0['x_position']}")
# the line of code above demonstrated how you can modify dictionaries using if-else blocks. 


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

# the 'del' statement removes a key-value pair in a dictionary
# removed the 'points' key-value from the 'alien_0' dictionary
del alien_0['points']
print(alien_0)

alien_0 = {'color': 'green', 'speed': 'slow'}

# The get() method will set a default value that will be returned when the requested key is not found in the dictionary.
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)


alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'yellow', 'points': 15}

# Here I created a list of dictionaries of different aliens for a video game
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

# Make an empty list for storing aliens
aliens = []

# using the range function it loops through this line of code 30 times
# range function is used to set the amount of times something should be looped
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	# adds these aliens to the blank alien list mentioned earlier.
	aliens.append(new_alien)

# This is showing how the 30 aliens that were created are all individual objects.
# Here we changed the first three aliens in the list to yellow with a medium speed and a point value of 10.
for alien in aliens[:3]:
	if alien['color'] =='green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = '10'

# Show the first 5 aliens.
# uses the [:] to slice the first 5 aliens
for alien in aliens [:5]:
	print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")