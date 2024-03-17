command = input().split(": ")
final_dict = {}

while command[0] != "statistics":
    key = command[0]
    value = int(command[1])
    if key not in final_dict:
        final_dict[key] = 0
    final_dict[key] += value
    command = input().split(": ")

print("Products in stock:")
for product in final_dict.keys():
    print(f"- {product}: {final_dict[product]}")
print(f"Total Products: {len(final_dict)}")
print(f"Total Quantity: {sum(qty for qty in final_dict.values())}")
