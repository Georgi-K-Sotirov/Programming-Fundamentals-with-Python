while True:
    string = input()
    if string == "SoftUni":
        continue
    if string == "End":
        break
    for index in range(len(string)):
        print(string[index] * 2, end="")
    print()