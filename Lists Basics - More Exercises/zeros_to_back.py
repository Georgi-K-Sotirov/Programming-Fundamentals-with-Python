number = [int(numbers) for numbers in input().split(", ")]

for current_number in number:
    if current_number == 0:
        number.remove(current_number)
        number.append(current_number)

print(number)