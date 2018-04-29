prompt = "\nPlease enter the name of city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.)"
active = True

while active:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
