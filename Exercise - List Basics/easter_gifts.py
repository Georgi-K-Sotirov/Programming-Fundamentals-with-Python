gifts = input().split()

while True:
    command_and_gift = input()
    if command_and_gift == "No Money":
        break
    command_and_gift = command_and_gift.split()
    command = command_and_gift[0]
    gift = command_and_gift[1]
    if command == "OutOfStock":
        gifts = [sub.replace(gift, "None") for sub in gifts]
    elif command == "Required":
        index = int(command_and_gift[2])
        if len(gifts) > index >= 0:
            gifts[index] = gift
    elif command == "JustInCase":
        gifts[-1] = gift

none_none_list = []
for current_gift in gifts:
    if current_gift != "None":
        none_none_list.append(current_gift)
print(" ".join(none_none_list))