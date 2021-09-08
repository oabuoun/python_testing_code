def read_value():
    num = input("Please enter a value: ")
    num = int(num)
    return num

def read_values():
    num1 = input("Please enter the first value: ")
    num1 = int(num1)
    num2 = input("Please enter the second value: ")
    num2 = int(num2)
    return num1, num2

def calc_sum(num1: int = 0, num2: int = 0):
    return num1 + num2

def calc_sub(num1, num2):
    return num1 - num2

calc_sub2 = lambda num1, num2: num1 - num2

'''
This is multiplication function
It will return a value
'''
def calc_mul(num1, num2):
    return num1 * num2

#   This is a division function
def calc_div(num1, num2):
    if num2 == 0:
        raise Exception("Sorry, num2 should not be equal to Zero")
        return "Operation Not Allowed"
    else:
        return num1 / num2

def calc_div2(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError as exception_zero:
        print(exception_zero)
        return None
    except Exception as general_exception:
        return None
    else:
        # no exception was raised
        print("The division was performed successfully")
    finally:
        # do something whenever you finished,  wether an exception is raised or not
        print("This is the finally block of code")
    return result

def print_result(num1, num2, operation, result, description = "No Description"):
    #print("Number1:", num1, operation, "Number2:", num2, "=" ,result)
    # text = "(Number1: {}) {} (Number2:{}) = {}".format(num1, operation, num2, result)
    text = f"(Number1: {num1}) {operation} (Number2: {num2}) = {result}  | {description}"
    print(text)

for index in range(0, 1):
    number1, number2 = read_values()

    sum = calc_sum(num1 = number1, num2 = number2)
    print_result(number1, number2, '+', sum, "This is a sum operation")

    sub = calc_sub(number1, number2)
    print_result(number1, number2, '-', sub)

    sub = calc_sub2(number1, number2)
    print_result(number1, number2, '-', sub, "Subtraction using Lambda")

    mul = calc_mul(number1, number2)
    print_result(number1, number2, '*', mul)

    assert number2 != 0, "Sorry, number2 should not be Zero (Using assert method)"
    div = calc_div(number1, number2)
    print_result(number1, number2, '/', div)
