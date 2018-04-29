# encoding=utf-8

class Dog():
    """a model of dogs"""
    
    def __init__(self,name,age):
        """initialize name, age"""
        self.name = name 
        self.age = age
        
    def sit(self):
        """a dog is commanded to sit"""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """a dog is commanded to roll over"""
        print(self.name.title(), "rolled over!")
        
my_dog = Dog('eilli', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + '.')
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + '.')
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.roll_over()
