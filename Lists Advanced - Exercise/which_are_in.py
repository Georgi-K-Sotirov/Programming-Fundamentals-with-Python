first_list = input().split(", ")
second_list = input().split(", ")
final_list = []

for chars in first_list:
    for word in second_list:
        if chars in word:
            final_list.append(chars)
            break

print(final_list)
 