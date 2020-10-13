# using a while loop with lists and dictionaries.
# start with users that need to be verified
# empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users =[]

# the loop continues until all unconfirmed users are moved to confirmed_users.
# this loop will keep running as long as unconfirmed_users is not empty.
while unconfirmed_users:
    # a current user is an uncomfirmed user.
    # the pop method removes a name fom the unconfirmed_users
    current_user = unconfirmed_users.pop()

    # the current_user is the popped unconfirmed user.
    print(f"Verifying user: {current_user.title()}")
    # adding the current_user to the confirmed_user list. 
    confirmed_users.append(current_user)

# displaying all the confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

