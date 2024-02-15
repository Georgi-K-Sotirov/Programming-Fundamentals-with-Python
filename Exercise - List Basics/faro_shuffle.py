my_list = input().split()
count = int(input())

half = len(my_list) // 2

for shuffles in range(count):
    left_half = my_list[:half:]
    right_half = my_list[half::]
    current_list = []
    for index in range(len(left_half)):
        current_list.append(left_half[index])
        current_list.append(right_half[index])
    my_list = current_list
print(my_list)
