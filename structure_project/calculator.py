from calc_package import calc_module
import json

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

def print_result(num1, num2, operation, result, description = "No Description"):
    #print("Number1:", num1, operation, "Number2:", num2, "=" ,result)
    # text = "(Number1: {}) {} (Number2:{}) = {}".format(num1, operation, num2, result)
    text = f"(Number1: {num1}) {operation} (Number2: {num2}) = {result}  | {description}"
    print(text)

data_list = []
for index in range(0, 3):
    data = {"number1": None, "number2": None, "sum": None, "sub": None, "sub2": None, "mul": None, "div": None}
    number1, number2 = read_values()
    data["number1"] = number1
    data["number2"] = number2

    sum = calc_module.calc_sum(num1 = number1, num2 = number2)
    print_result(number1, number2, '+', sum, "This is a sum operation")
    data["sum"] = sum
    #file.write(f"sum = {sum}\n")

    sub = calc_module.calc_sub(number1, number2)
    print_result(number1, number2, '-', sub)
    data["sub"] = sub
    #file.write(f"sub = {sub}\n")

    sub = calc_module.calc_sub2(number1, number2)
    print_result(number1, number2, '-', sub, "Subtraction using Lambda")
    data["sub2"] = sub
    #file.write(f"sub2 = {sub}\n")

    mul = calc_module.calc_mul(number1, number2)
    print_result(number1, number2, '*', mul)
    data["mul"] = mul
    #file.write(f"mul = {mul}\n")

    assert number2 != 0, "Sorry, number2 should not be Zero (Using assert method)"
    div = calc_module.calc_div(number1, number2)
    print_result(number1, number2, '/', div)
    data["div"] = div
    #file.write(f"div = {div}\n")

    print(data)
    data_list.append(data)

print(data_list)
with open("log-solution1-py.json", "w") as file:
    json.dump(data_list, file, indent = 4)

with open("log-solution1-py.json", "r") as file:
    imported_data = json.load(file)
    print(imported_data)
