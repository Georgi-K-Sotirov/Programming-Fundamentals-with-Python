def max_number(nums):
    return max(nums)


def min_number(numbers):
    return min(numbers)


def sum_numbers(numbers):
    return sum(numbers)


numbers = list(map(int, input().split(" ")))

print(f"The minimum number is {min_number(numbers)}")
print(f"The maximum number is {max_number(numbers)}")
print(f"The sum number is: {sum_numbers(numbers)}")
