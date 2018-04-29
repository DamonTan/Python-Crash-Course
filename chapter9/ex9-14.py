from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides
        
    def roll_die(self, times):
        i = 1
        while i <= times:
            print("The result of No." + str(i) + " is " + str(randint(1,self.sides)))
            i += 1
        print('\n')
            
die_with_6sides = Die()
die_with_6sides.roll_die(10)

die_with_10sides = Die(10)
die_with_10sides.roll_die(10)

die_with_20sides = Die(20)
die_with_20sides.roll_die(10)
