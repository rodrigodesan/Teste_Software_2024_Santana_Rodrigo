from functools import reduce

class Calculator:
    @staticmethod
    def sum(*numbers):
        return reduce(lambda x, y: x + y, numbers)

    @staticmethod
    def substract(*numbers):
        return reduce(lambda x, y: x - y, numbers)

    @staticmethod
    def multiply(*numbers):
        return reduce(lambda x, y: x * y, numbers)

    @staticmethod
    def divide(*numbers):
        return reduce(lambda x, y: x / y, numbers)

if __name__ == '__main__':
    print(Calculator.sum(2, 1, 5))
    print(Calculator.substract(5, 1, 4))
    print(Calculator.multiply(2, 1, 5))
    print(Calculator.divide(10, 2))
