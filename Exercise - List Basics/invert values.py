my_list = input().split()
invert_list = []

for current_number in my_list:
    invert_list.append(-int(current_number))

print(invert_list)