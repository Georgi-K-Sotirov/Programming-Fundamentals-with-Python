def sum_numbers(num1, num2):
    return num1 + num2


def subtract(a, b):
    return a - b


def add_and_subtract(num1, num2, num3):
    result = sum_numbers(num1, num2)
    return subtract(result, num3)


num1, num2, num3 = int(input()),  int(input()), int(input())
print(add_and_subtract(num1, num2, num3))