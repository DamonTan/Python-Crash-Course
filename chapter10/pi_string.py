filename = 'pi_million_digits.txt'

with open(filename, encoding='UTF-8') as file_object:
    lines = file_object.readlines()

pi_string = ''
pi_number = ''
numbers = ['0','1','2','3','4','5','6','7','8','9','.']

for line in lines:
    pi_string += line.rstrip()

for pi in pi_string:
    if pi in numbers:
        pi_number += pi 
    
print(pi_number[:52] + '......')
print(len(pi_number))

#birthday = input("Enter your birthday, in the form mmddyy: ")
#if birthday in pi_string:
#    print("Your birthday appears in the first million digits of pi!")
#else:
#    print("Your birthday does not appear in the first million digits of pi.")
#
