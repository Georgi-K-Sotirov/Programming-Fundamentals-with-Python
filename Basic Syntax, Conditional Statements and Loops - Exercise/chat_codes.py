number_of_messages = int(input())

for _ in range(number_of_messages):
    number_code = int(input())
    if number_code == 88:
        print("Hello")
    elif number_code == 86:
        print("How are you?")
    elif number_code < 88:
        print("GREAT!")
    else:
        print("Bye.")
