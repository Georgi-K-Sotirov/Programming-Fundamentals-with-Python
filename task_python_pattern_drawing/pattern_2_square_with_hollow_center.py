number = int(input())

for i in range(1, number+1):
    if i == 1 or i == number:
        print("*" * number)
        continue
    print("*" + (' ' * (number-2)) + "*")