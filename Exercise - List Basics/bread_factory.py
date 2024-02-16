working_days = input().split("|")
energy = 100
coins = 100

closed_bakery = False
for current_day in working_days:
    current_event_and_number = current_day.split("-")
    current_event = current_event_and_number[0]
    current_number = int(current_event_and_number[1])
    current_energy = 0
    if current_event == "rest":
        current_energy = current_number + energy
        if current_energy > 100:
            current_energy = 100
        gained_energy = abs(current_energy - energy)
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {current_energy}.")
        energy = current_energy
    elif current_event == "order":
        if energy < 30:
            energy += 50
            print("You had to rest!")
            continue
        else:
            energy -= 30
            coins += current_number
            print(f"You earned {current_number} coins.")
    else:
        if coins >= current_number:
            coins -= current_number
            print(f"You bought {current_event}.")
        else:
            closed_bakery = True
            print(f'Closed! Cannot afford {current_event}.')
            break
if not closed_bakery:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")