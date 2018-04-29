class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print("This restaurant's name is " + self.name.title() + ".")
        print("It's a " + self.cuisine.title() + " restaurant.")
        
    def open_restaurant(self):
        print(self.name.title() + ' is open now!')
        
    def set_number_served(self, numbers):
        self.number_served = numbers
        
    def increment_number_served(self, numbers):
        self.number_served += numbers
        
restaurant = Restaurant('uncle pizza', 'americian')

print(restaurant.name.title())
print(restaurant.cuisine.title())

restaurant.set_number_served(10)

print("There are " + str(restaurant.number_served) + " seats reserved.")

restaurant.increment_number_served(100)
print(restaurant.number_served)

restaurant.describe_restaurant()
restaurant.open_restaurant()

