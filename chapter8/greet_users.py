def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
        
usernames = ['damon','steven','alice']
greet_users(usernames)
