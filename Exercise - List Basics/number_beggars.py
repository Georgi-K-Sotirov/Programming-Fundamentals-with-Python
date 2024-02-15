coins = input().split(", ")
beggars = int(input())
starting_index = 0
beggars_coins = []

for current_beggar in range(beggars):
    current_beggar_coins = 0
    for current_index in range(starting_index, len(coins), beggars):
        current_beggar_coins += int(coins[current_index])
    beggars_coins.append(current_beggar_coins)
    starting_index += 1

print(beggars_coins)