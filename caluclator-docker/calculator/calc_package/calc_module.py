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
