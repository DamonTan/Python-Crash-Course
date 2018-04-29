def get_formatted_name(first_name,last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
    
flag = True
while flag:
    print("\nPlease enter your name: ")
    print("(enter 'q' or 'quit' to quit!)")
    f_name = input("First name: ")
    if f_name == "quit" or f_name == 'q':
        break
    l_name = input("Last_name: ")
    if l_name == 'quit' or l_name == 'q':
        break
        
    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello, " + formatted_name + "!")
