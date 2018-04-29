rivers = {'nile': 'egypt','yangtz': 'china','amazon': 'brazil'}
for river, country in rivers.items():
    print(river.title() + " runs through " + country.title() + ".")
    
for river in rivers.keys():
    print(river.title())
    
for country in rivers.values():
    print(country.title())
