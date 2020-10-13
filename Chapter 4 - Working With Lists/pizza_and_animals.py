pizzas = ['pinapple', 'jalapeno', 'cheese']
for pizza in pizzas:
	print(f"I like {pizza.title()} pizza.\n")

print("I really love pizza!\n")

animals = ['cat', 'dog', 'bird']
for animal in animals:
	print(f"A {animal.title()} would make a great pet.\n")

print("Any of these animals would make a great pet.")

friend_pizzas = pizzas[:]
pizzas.append('pepporoni')
friend_pizzas.append('onions')
print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)