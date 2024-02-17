from math import inf

my_list = [int(x) for x in input().split(" ")]


while True:
    max_number = -inf
    min_number = inf
    command_list = input().split(" ")
    command_type = command_list[0]
    if command_type == "exchange":
        command_index = int(command_list[1])
        if 0 <= command_index < len(my_list):
            my_list = my_list[command_index + 1::] + my_list[:command_index + 1:]
        else:
            print("Invalid index")
    elif command_type == "max":
        even_or_odd = command_list[1]
        if even_or_odd == "even":
            max_even_index = -1
            for index in range(len(my_list)):
                if my_list[index] % 2 == 0:
                    if my_list[index] >= max_number:
                        max_even_index = index
                        max_number = my_list[index]
            if max_even_index >= 0:
                print(max_even_index)
            else:
                print("No matches")
        elif even_or_odd == "odd":
            max_odd_index = -1
            for index in range(len(my_list)):
                if my_list[index] % 2 != 0:
                    if my_list[index] >= max_number:
                        max_odd_index = index
                        max_number = my_list[index]
            if max_odd_index >= 0:
                print(max_odd_index)
            else:
                print("No matches")
    elif command_type == "min":
        even_or_odd = command_list[1]
        if even_or_odd == "even":
            min_even_index = -1
            for index in range(len(my_list)):
                if my_list[index] % 2 == 0:
                    if my_list[index] <= min_number:
                        min_even_index = index
                        min_number = my_list[index]
            if min_even_index >= 0:
                print(min_even_index)
            else:
                print("No matches")
        elif even_or_odd == "odd":
            min_odd_index = -1
            for index in range(len(my_list)):
                if my_list[index] % 2 != 0:
                    if my_list[index] <= min_number:
                        min_odd_index = index
                        min_number = my_list[index]
            if min_odd_index >= 0:
                print(min_odd_index)
            else:
                print("No matches")
    elif command_type == "first":
        print_list = []
        count_number = int(command_list[1])
        command_type = command_list[2]
        if 0 <= count_number > len(my_list):
            print("Invalid count")
            continue
        if command_type == "even":
            for current_number in my_list:
                if current_number % 2 == 0:
                    print_list.append(current_number)
        elif command_type == "odd":
            for current_number in my_list:
                if current_number % 2 != 0:
                    print_list.append(current_number)
        print(print_list[:count_number:])
    elif command_type == "last":
        print_list = []
        count_number = int(command_list[1])
        command_type = command_list[2]
        if 0 <= count_number > len(my_list):
            print("Invalid count")
            continue
        if command_type == "even":
            for current_number in my_list:
                if current_number % 2 == 0:
                    print_list.append(current_number)
        elif command_type == "odd":
            for current_number in my_list:
                if current_number % 2 != 0:
                    print_list.append(current_number)
        print(print_list[- count_number::])
    elif command_type == "end":
        print(my_list)
        break