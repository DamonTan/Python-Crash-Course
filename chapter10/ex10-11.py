import json

def get_new_number():
    filename = 'favorite_number.json' 
    numbers = input("What is your favorite numbers?\n")
    with open(filename, 'w') as f_obj:
        json.dump(numbers, f_obj)
    return numbers
        
def get_stored_number():
    filename = 'favorite_number.json'
    try:
        with open(filename) as f_obj:
            numbers = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return numbers

def favorite_number():
    numbers = get_stored_number()
    if numbers:
        print("I know your favorite number! It's " + numbers + ".")
    else:
        numbers = get_new_number()
        print("Your favorite number is " + numbers + ".")
        
favorite_number()
