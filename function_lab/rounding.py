def rounding(list):
    new_list = []
    for current_number in list:
        new_list.append(round(current_number))
    return new_list

nums = map(float, input().split())

res = rounding(nums)
print(res)