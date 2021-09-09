
class CalculatorClass:
    op_count = 0

    @classmethod
    def add_op(cls):
        cls.op_count += 1

    def __init__(self, number1, number2):
        self.num1 = number1
        self.num2 = number2

    def add(self):
        self.add_op()
        return self.num1 + self.num2

    def subtract(self):
        self.add_op()
        return self.num1 - self.num2
