from math import floor
number = int(input())

for r in range(1, number + 1, 2):
        print((" " * floor((number - r)/2)) + ("*" * r))
for r in range(number - 2, -1, -2):
        print((" " * floor((number - r)/2)) + ("*" * r))
