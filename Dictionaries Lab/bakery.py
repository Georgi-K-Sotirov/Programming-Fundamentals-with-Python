food_and_quantities = input().split()
final_dict = {}
for index in range(0, len(food_and_quantities),2):
    product = food_and_quantities[index]
    qty = int(food_and_quantities[index + 1])
    final_dict[product] = qty

print(final_dict)