numbers = range(1,21)
for number in numbers:
	print(number)

numbers = range (1, 1000001)
#for number in numbers:
	#print(number)

numbers = list(range(1, 1000000))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

even_numbers = list(range(1, 20, 2))
print(even_numbers)

multiples = []
for multiple in range(3,31):
	three = multiple**3
	multiples.append(three)
print(multiples)

cubes = []
for cube in range(1,11):
	cubed = cube**3
	cubes.append(cubed)
print(cubes)

cubes = [cube**3 for cube in range(1,11)]
print(cubes)