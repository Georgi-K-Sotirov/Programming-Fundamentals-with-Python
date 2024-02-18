def absolute_values(list):
    new_list = []
    for current_number in list:
        new_list.append(abs(current_number))
    return new_list


numbers_list = (map(float, input().split()))

print(absolute_values(numbers_list))
