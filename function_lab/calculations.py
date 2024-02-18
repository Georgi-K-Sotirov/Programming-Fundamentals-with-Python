def calculator(command,a, b):
    if command == "multiply":
        return a * b
    elif command == "divide":
        if b != 0:
            return int(a / b)
        else:
            return print("Division by 0")
    elif command == "add":
        return a + b
    elif command == "subtract":
        return  a - b

command = input()
first_num = int(input())
second_num = int(input())

res = calculator(command, first_num, second_num)
print(res)