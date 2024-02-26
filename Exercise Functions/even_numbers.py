def check_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


numbers = map(int, input().split(" "))

result = list(filter(check_even, numbers))
print(result)
