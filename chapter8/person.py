def build_person(first_name,last_name,age=''):
    """return a dictionaary containing information of a certain person"""
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person
    
musician = build_person('damon','tan',27)
print(musician)

author = build_person('alice','gao')
print(author)
