number_list = list(map(int, input().split(", ")))

found_index = map(lambda i: i if number_list[i] % 2 == 0 else 'no', range(len(number_list)))

final_list = list(filter(lambda x: x != "no", found_index))

print(final_list)