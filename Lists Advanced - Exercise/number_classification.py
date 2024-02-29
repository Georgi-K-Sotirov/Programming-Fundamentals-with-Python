def positive(nums):
    result = [str(num) for num in nums if num >= 0]
    return ", ".join(result)


def negative(nums):
    result = [str(num) for num in nums if num < 0]
    return ", ".join(result)


def even(nums):
    result = [str(num) for num in nums if num % 2 == 0]
    return ", ".join(result)


def odd(nums):
    result = [str(num) for num in nums if num % 2 != 0]
    return ", ".join(result)


numbers_list = [int(num) for num in input().split(", ")]
print(f"Positive: {positive(numbers_list)}")
print(f"Negative: {negative(numbers_list)}")
print(f"Even: {even(numbers_list)}")
print(f"Odd: {odd(numbers_list)}")