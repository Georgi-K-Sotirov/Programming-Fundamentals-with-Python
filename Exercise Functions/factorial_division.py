def factorial_division(num):
    result = 1
    for digit in range(1, num + 1):
        result *= digit

    return result


first_num = int(input())
second_num = int(input())

print(f"{factorial_division(first_num)/factorial_division(second_num):.2f}")
