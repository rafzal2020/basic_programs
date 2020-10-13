height = input("How tall are you, in inches? ")
height = int(height)
# the int() function is useful when interpreting numbers
# without the int() function, python would not allow you to interpret numbers

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou're not tall enough to ride... loser.")
