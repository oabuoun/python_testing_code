import calculator

number1 = input("Please Enter The First Number:  ")
number1 = int(number1)
number2 = input("Please Input The Second Number: ")
number2 = int(number2)

calculatorObject = calculator.CalculatorClass(number1, number2)
sum = calculatorObject.add()
print(sum)

sub = calculatorObject.subtract()
print(sub)
