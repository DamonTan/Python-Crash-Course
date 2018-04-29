class Car():
    """a try to simulate cars"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year 
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name  = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()
        
    def read_odometer(self):
        """print message about odometer"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """update odometer, and forbiden any tempt to roll back odometer"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        
    def increment_odometer(self, miles):
        """increase odometer with a certain increment"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")
            
    def fill_gas_tank(self, numbers):
        print("Please fill " + str(numbers) + "-L gas for my car.")
        
class Battery():
    """a simulation of electriccar's battery"""
    
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """especially for electric cars"""
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def describle_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWh battery.")
        
    def fill_gas_tank(self, numbers):
        print("This car doesn't need a gas tank!")
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()

my_tesla.battery.get_range()
