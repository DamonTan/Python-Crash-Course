def get_formatted_site(city, country, population=''):
    if population:
        formatted_site = city + " " + country
        formatted_pop = ' - population ' + str(population)
    else:
        formatted_site = city + " " + country
        formatted_pop = ''
        
    return formatted_site.title() + formatted_pop
