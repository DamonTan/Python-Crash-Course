def build_profile(first, last, **user_info):
    """build a dictionary which contains everything we know about user"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
    
user_profile1 = build_profile('albert', 'einstein', location='princeton', field='physics')
print('\n', user_profile1)

user_profile2 = build_profile('damon', 'tan', university='NJU', age=27)
print('\n', user_profile2)
