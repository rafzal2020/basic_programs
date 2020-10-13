dimensions = (200,50)
# this list is known as a Tuple. A tuple cannot be changed and it is different from a list as it is made using parentheses instead of brackets.
print(dimensions[0])
print(dimensions[1])

###	dimensions[0] = 250
#Look how an error is displayed when we try to change the item value in this tuple. This proves that tuples are always constant. 
print("Orignial Dimensions:")
for dimension in dimensions:
	print(dimension)
	# you can use tuples in a for loop as shown here. 

dimensions = (400, 100)
print("\nModified Dimensions:")
for dimension in dimensions:
	print(dimension)

# With this line of code, you can see how you can still change the value in a tuple. You can assign a new value to a variable that represents a tuple. 