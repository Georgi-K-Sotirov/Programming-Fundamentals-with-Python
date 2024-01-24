key = int(input())
number_letters = int(input())

for index in range(number_letters):
    current_letter = input()
    current_letter = ord(current_letter)
    print(chr(key + current_letter), end="")