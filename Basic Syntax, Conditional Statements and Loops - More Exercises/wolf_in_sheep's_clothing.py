word = input()
list = word.split(", ")

for index in range(len(list)):
    if list[index] == "wolf":
        if index == len(list) - 1:
            print("Please go away and stop eating my sheep")
        else:
            print(f"Oi! Sheep number {len(list) - 1 - index}! You are about to be eaten by a wolf!")