year = int(input())

while True:
    year += 1
    check = ""
    for digit in str(year):
        if digit in check:
            break
        else:
            check += digit
    else:
        print(check)
        break
