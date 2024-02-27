def palindrome(numbers):
    result = ''
    for nums in numbers:
        if nums == nums[::-1]:
            result += 'True\n'
        else:
            result += 'False\n'
    return result


number = input().split(", ")
print(palindrome(number))