def sum_of_odd_digits(number):
    result = 0
    for digit in str(number):
        if int(digit) % 2 != 0:
            result += int(digit)
    return result


def sum_of_even_digits(number):
    result = 0
    for digit in str(number):
        if int(digit) % 2 == 0:
            result += int(digit)
    return result


number = int(input())
print(f'Odd sum = {sum_of_odd_digits(number)}, Even sum = {sum_of_even_digits(number)}')