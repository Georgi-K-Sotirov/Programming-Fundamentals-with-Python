def perfect_number(number):
    digit_sum = 0

    for digit in range(1, number + 1):
        if number % digit == 0:
            digit_sum += digit

    if (digit_sum / 2) == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())
perfect_number(number)