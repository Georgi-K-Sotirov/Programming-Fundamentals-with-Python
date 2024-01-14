quantity = int(input())
days = int(input())
ornament_price = 2
tree_skirt = 5
tree_garland = 3
tree_light = 15
total_coast = 0
christmas_points = 0

for current_day in range(1, days +1):
    if current_day % 11 == 0:
        quantity += 2
    if current_day % 2 == 0:
        total_coast += quantity * ornament_price
        christmas_points += 5
    if current_day % 3 == 0:
        total_coast += quantity * (tree_skirt + tree_garland)
        christmas_points += 13
    if current_day % 5 == 0:
        total_coast += quantity * tree_light
        christmas_points += 17
        if current_day % 3 == 0:
            christmas_points += 30
    if current_day % 10 == 0:
        christmas_points -= 20
        total_coast += tree_light + tree_garland + tree_skirt
if days % 10 == 0:
    christmas_points -= 30
print(f"Total cost: {total_coast}")
print(f"Total spirit: {christmas_points}")