def get_formatted_name(first_name,last_name,middle_name=''):
    """return formatted full name"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()
    
musician = get_formatted_name('damon','james','tan')
print(musician)
engineer = get_formatted_name('damon','tan')
print(engineer)
