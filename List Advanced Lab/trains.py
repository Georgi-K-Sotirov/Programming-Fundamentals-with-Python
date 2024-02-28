wagons = [0] * int(input())

while True:
    command_input = input().split()
    command = command_input[0]

    if command == "End":
        print(wagons)
        break
    elif command == "add":
        people = int(command_input[1])
        wagons[-1] += people
    elif command == "insert":
        index = int(command_input[1])
        people = int(command_input[2])
        wagons[index] += people
    elif command == "leave":
        index = int(command_input[1])
        people = int(command_input[2])
        wagons[index] -= people