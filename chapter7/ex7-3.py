number = input("Enter a number, and I will tell you if it's times of 10: ")
number = int(number)

if number % 10 == 0:
    print(number, "is times of 10.")
else:
    print(number, "is not times of 10.")
