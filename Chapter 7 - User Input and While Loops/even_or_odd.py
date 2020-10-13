number = input("Eter a number, and I'll tell you if it's even or odd: ")
number = int(number)

# this will be an even number because all even numbers are divisible by 2.
if number % 2 == 0:
    # the # operator is called the modulo operator
    # it is used for finding the remainder of the quotient of two numbers
    # the % operator ONLY returns the remainder, nothing else.
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
