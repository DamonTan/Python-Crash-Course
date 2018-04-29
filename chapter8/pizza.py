def make_pizza(size, *toppings):
    """print all toppings of a pizza"""
    print('\nMaking a ' + str(size) + '-inch pizza with the following topppings:')
    for topping in toppings:
        print('- ' + topping)
