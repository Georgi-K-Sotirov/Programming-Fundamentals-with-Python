numbers = input().split()
input_string = input()
message = []

for num in numbers:
    index = sum(int(digit) for digit in num)
    if index >= len(input_string):
        index %= len(input_string)
    message.append(input_string[index])
    input_string = input_string[:index] + input_string[index + 1:]

print("".join(message))
