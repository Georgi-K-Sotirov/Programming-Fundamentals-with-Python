number = int(input())
tank_capacity = 255

for current_operation in range(number):
    current_liters = int(input())
    if tank_capacity < current_liters:
        print("Insufficient capacity!")
        continue
    tank_capacity -= current_liters
print(f"{255 - tank_capacity}")