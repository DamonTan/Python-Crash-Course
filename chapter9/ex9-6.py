class Restaurant():
    """a simulation of restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        
    def describe_restaurant(self):
        print("This restaurant's name is " + self.name.title() + ".")
        print("It's a " + self.cuisine.title() + " restaurant.")
        
    def open_restaurant(self):
        print(self.name.title() + ' is open now!')

class Icecreamstand(Restaurant):
    """a simulation of ice cream stand"""
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['sweet', 'apple', 'mango']
    
    def describle_icecream(self):
        print("This ice cream stand has kinds of icecreams, such as ")
        for i in self.flavors:
            print(i)

        
icecream = Icecreamstand('uncle cream', 'sweetee')
icecream.describle_icecream()

