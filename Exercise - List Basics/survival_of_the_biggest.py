from math import inf

number = [int(numbers) for numbers in input().split()]
counter = int(input())

for index in range(counter):
    small_number = inf
    for current_number in number:
        if current_number < small_number:
            small_number = current_number
    number.remove(small_number)
number_as_str = [str(current_number) for current_number in number]
print(", ".join(number_as_str))