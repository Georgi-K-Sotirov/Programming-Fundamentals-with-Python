fire_type_and_value = input().split("#")
water = int(input())
effort = 0
total_fire = 0
put_out_cells = []
for current_cell in fire_type_and_value:
    current_fire_type_and_value = current_cell.split(" = ")
    current_type = current_fire_type_and_value[0]
    current_value = int(current_fire_type_and_value[1])
    if ((current_type == "High" and 81 <= current_value <= 125) or
            (current_type == "Medium" and 51 <= current_value <= 80) or
            (current_type == "Low" and 1 <= current_value <= 50)):
        if water >= current_value:
            water -= current_value
            put_out_cells.append(str(current_value))
            effort += current_value * 0.25
            total_fire += current_value

print("Cells:")
if len(put_out_cells) >= 1:
    print("\n".join([f" - {cell}" for cell in put_out_cells]))
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
