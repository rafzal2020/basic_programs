message = "\nWhat is your age? "
age = ""


while age != 0:
    age = input(message)
    age = int(age)
    if age < 3:
        print("Your ticket is free")
    elif age <= 12:
        print("The price of your ticket is $10.")
    elif age > 12:
        print("The price of your ticket is $15.")
    elif age == 0:
        print("Okay.")
        break
    

