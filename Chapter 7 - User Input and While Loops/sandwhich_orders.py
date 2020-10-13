sandwhich_order = ['balogne', 'peanut butter', 'egg salad', 'pastrami', 'pastrami', 'pastrami']
finished_sandwhiches = []

print("\nWe are out of pastrami")
while 'pastrami' in sandwhich_order:
    sandwhich_order.remove('pastrami')

while sandwhich_order:
    made_sandwhiches = sandwhich_order.pop()
    print(f"\nMade your {made_sandwhiches} sandwhich.")
    finished_sandwhiches.append(made_sandwhiches)

print("\nThe following sandwhiches have been made:")
for finished_sandwhich in finished_sandwhiches:
    print(finished_sandwhich)
