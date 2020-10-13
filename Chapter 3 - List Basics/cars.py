cars = ['bmw', ' audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# the sort() method sorts a list in alphabetical order PERMANENTLY

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
# the reverse=True statement makes the list in alphabetical order.

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the orignial list.")
print(cars)

print("\nHere is the sorted list")
print(sorted(cars))
# the sorted() method sorts the list TEMPORARILY instead of permanently.

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)
# The reverse() method flips the order of the list. NOTE: It does not flip the list in alphabetical order like the "reverse=True" statement does. 

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
# The len() function can be used to determine the number of contents in the list. In this case, the len is 4
