motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
#you can replace elements in a list using the line of code shown above. motorcycle[0] changed the first item in the list to a new item. 

motorcycles.append('ducati')
print(motorcycles)
#.append() method allows you to add an item to a list.

motorcycles = []
#leaving the list blank is useful for adding items to a list via user input. 

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
#appending all these items will add it to the blank list. 

print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)
#The insert() method allows you to add an item to a list at any position. Here, we added ducati to position 0; but we can also add it to position 1, 2 , or 3. 

del motorcycles[0]
print(motorcycles)
#the "del" statement allows you to remove an item from a list. In this case, we removed the item in position 0 in the list. 

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
#variable used to store the popped item in the list.
print(motorcycles)
print(popped_motorcycle)
#the pop() method removes the last item in a list but that item will still have value in the program. 

first_owned = motorcycles.pop(0)
print(f'The first motorcycle I owned was a {first_owned.title()}.')

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
# the .remove() method allows you to remove an item from a list without knowing its position number. You can just name it to remove it. 

print(f"\nA {too_expensive.title()} is too expensive for me.")

