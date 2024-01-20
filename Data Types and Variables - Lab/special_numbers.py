number = int(input())
for current_number in range(1, number + 1):
    sum_digit = 0
    for digit in str(current_number):
        sum_digit += int(digit)
    if sum_digit == 5 or sum_digit == 7 or sum_digit == 11:
        print(f"{current_number} -> True")
    else:
        print(f"{current_number} -> False")
