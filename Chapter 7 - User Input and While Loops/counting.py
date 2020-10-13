current_number = 0
# setting a variable to store a number
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        # if the remainder of the quotient of the number and 2 is 0, continue.
        # the continue statement begins the loop again.
        continue

    print(current_number)
    # prints odd numbers from 0-10 only. 
