class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        
    def describe_restaurant(self):
        print("This restaurant's name is " + self.name.title() + ".")
        print("It's a " + self.cuisine.title() + " restaurant.")
        
    def open_restaurant(self):
        print(self.name.title() + ' is open now!')
        
restaurant = Restaurant('uncle pizza', 'americian')

print(restaurant.name.title())
print(restaurant.cuisine.title())

restaurant.describe_restaurant()
restaurant.open_restaurant()
