def valid_index(index):
    if 0 <= index < len(list_of_names):
        return True
    else:
        return False


list_of_names = input().split(", ")
blacklist_counter = 0
error_counter = 0

while True:
    command = input().split()
    command_type = command[0]

    if command_type == "Blacklist":
        searched_name = command[1]
        if searched_name in list_of_names:
            blacklist_counter += 1
            print(f"{searched_name} was blacklisted.")
            list_of_names = [name.replace(searched_name, "Blacklisted") for name in list_of_names]
        else:
            print(f"{searched_name} was not found.")
    elif command_type == "Error":
        index = int(command[1])
        if valid_index(index):
            if list_of_names[index] != "Blacklisted" and list_of_names[index] != "Lost":
                error_counter += 1
                print(f"{list_of_names[index]} was lost due to an error.")
                list_of_names[index] = "Lost"
    elif command_type == "Change":
        index = int(command[1])
        new_name = command[2]
        if valid_index(index):
            print(f"{list_of_names[index]} changed his username to {new_name}.")
            list_of_names[index] = new_name
    elif command_type == "Report":
        print(f"Blacklisted names: {blacklist_counter}")
        print(f"Lost names: {error_counter}")
        print(" ".join(list_of_names))
        break
