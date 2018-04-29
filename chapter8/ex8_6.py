def city_country(city,country):
    """return city and its resposible country"""
    info = city.title() + ', ' + country.title()
    return info
    
one = city_country('nanjing','china')
print(one)
two = city_country('new york', 'USA')
print(two)
three = city_country(country='japan',city='tokyo')
print(three)
