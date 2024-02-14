number = int(input())

initial_list = []
for i in range(number):
    data = int(input())
    initial_list.append(data)

command = input()
filter_list = []

for i in range(len(initial_list)):
    if command == "even":
        if initial_list[i] % 2 == 0:
            filter_list.append(initial_list[i])
    elif command == "odd":
        if initial_list[i] % 2 != 0:
            filter_list.append(initial_list[i])
    elif command == "negative":
        if initial_list[i] < 0:
            filter_list.append(initial_list[i])
    elif command == "positive":
        if initial_list[i] >= 0:
            filter_list.append(initial_list[i])

print(filter_list)