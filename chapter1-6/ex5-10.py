current_users = ['damon', 'admin', 'gao', 'alice', 'tan']
new_users = ['damon', 'alice', 'steven', 'jeffry', 'tom']

for new_user in new_users:
    if new_user in current_users:
        print("Sorry, the user name has been registerd by other person. \
Please enter a new name.\n")
    else:
        print(new_user, "is your user name now.\n")

