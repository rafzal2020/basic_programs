dinner_guests = ['kanye west', 'playboi carti', 'frank ocean']
message_kanye = f"Hello, {dinner_guests[0].title()}, what is up?"
message_carti = f"Drop Whole Lotta Red, {dinner_guests[1].title()}."
message_frank = f"Want some bread, {dinner_guests[-1].title()}?"
print(message_frank)
print(message_carti)
print(message_kanye)

print(dinner_guests[2].title())

dinner_guests[2] = 'flight reacts'
print(dinner_guests)
message_flight = f"What it do, {dinner_guests[2].title()}."
print(message_flight)

print(f"I found a bigger dinner table, {dinner_guests}!")
dinner_guests.insert(0, 'james charles')
dinner_guests.insert(1, 'anderson paak')
dinner_guests.append('kendrick lamar')

print(dinner_guests)

print("I can only invite two people")

not_invited = dinner_guests.pop(0)
print(f"Sorry, {not_invited.title()}, you are not invited")
not_invited1 = dinner_guests.pop(0)
print(f"Sorry, {not_invited1.title()}, you are not invited")
not_invited2 = dinner_guests.pop(0)
print(f"Sorry, {not_invited2.title()}, you are not invited")
not_invited3 = dinner_guests.pop(0)
print(f"Sorry, {not_invited3.title()}, you are not invited")

print(dinner_guests)

del dinner_guests[0]
del dinner_guests[0]
print(dinner_guests)

print(len(dinner_guests))