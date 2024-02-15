factor = int(input())
count = int(input())
my_list = []

for current_number in range(1, count + 1):
    my_list.append(current_number * factor)

print(my_list)