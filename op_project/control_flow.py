number1 = input("Please enter a number: ")

number1 = int(number1)

if number1 == 0:
    print("You entered a zero and you cannot do a division by this number")
elif number1 > 0:
    print("You entered a positive number")
else:
    print("You entered a negative number")
