login_users = []
#login_users = ['damon', 'admin', 'gao', 'alice', 'tan']
if login_users:
    for login_user in login_users:
        if login_user == 'admin':
            print("Hello admin, would you like to see a status report?\n")
        else:
            print("Hello Eric, thank you for logging in again.\n")
else:
    print("We need to find some users!")
