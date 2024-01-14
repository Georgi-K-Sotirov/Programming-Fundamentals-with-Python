first_string = input()
second_string = input()
last_printed_string = first_string
for index in range(len(first_string)):
    left_string = second_string[:index + 1]
    right_stirng = first_string[index + 1:]
    new_string = left_string + right_stirng
    if new_string == last_printed_string:
        continue
    print(new_string)
    last_printed_string = new_string
