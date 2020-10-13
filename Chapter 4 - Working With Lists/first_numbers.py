for value in range(1, 5):
	print(value)
	# the "range()" function allows you to print a set of numbers within the given range
	# Also, notice how the program only prints the numbers 1-4. It does not count the 5 because this an example of an off-by-one behavior. 
numbers = list(range(1, 6))
print(numbers)
# the list() function allows you to print a range of given numbers in the form of a list. 

even_numbers = list(range(2,11,2))
print(even_numbers)
# adding a 3rd number in the range() function means that number will be used as an addition in the range. Meaning that 2 at the end means +2. Hence, it will print only even numbers within the range.

#using exponents to make a list of numbers 1-10 with exponent of 2.
squares = []
# start with a blank list with a variable name of squares
for value in range(1, 11):
	# the range is (1,11) or in other words 1-10
	square = value ** 2
	#every value in the list will be brought to the power of 2
	squares.append(square)
	#everytime the value is calculated, it is stored in the blank list. It will keep doing this until it reaches the range's limit.

print(squares)
#Prints the list after everything is done

# you can also write this line of code as squares.append(value**2). this is different because we stored the "value**2" in a variable but it can also be done in this way. 

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
#the min() function allows you to find the minimum value in a list of numbers
print(max(digits))
#the max() function allows you to find the maximum value in a list of numbers
print(sum(digits))
#the sum() function allows you to find the sum of all values in a list of numbers.

squares = [value**2 for value in range(1,11)]
print(squares)
#this line of code is the same as the 4 lines of code presented earlier except it is all done in just one line of code. 