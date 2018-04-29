print("Give me two numbers,, and I will add them togather.")
print("Enter 'q' to quit")

while True:
    try:
        a = input("\nEnter the first number: ")
        if a == 'q':
            break
        b = input("Enter the second number: ")
        if b == 'q':
            break
        answer = int(a) + int(b)
    except ValueError:
        print("You can't enter a string for addition!")
    else:
        print("The sum of " + str(a) + " and " + str(b) + " is " + str(answer))
