number = input("Enter a number, and I will tell you if it's evne or odd: ")
number = int(number)

if number % 2 == 0:
    print(str(number), "is even.")
else:
    print(str(number), "is odd.")
