def make_sandwich(*toppings):
    """print the toppings of sandwich which are unique to every customer"""
    print('\nThe sandwich is made of:')
    for topping in toppings:
        print('- ' + topping)
        
make_sandwich('egg')
make_sandwich('bacon','vegetable')
make_sandwich('ham','cheese','bread')
