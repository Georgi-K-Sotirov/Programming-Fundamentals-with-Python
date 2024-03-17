food_and_quantities = input().split()
final_dict = {}
for index in range(0, len(food_and_quantities),2):
    product = food_and_quantities[index]
    qty = int(food_and_quantities[index + 1])
    final_dict[product] = qty

products_surch = input().split()
for prod in products_surch:
    if prod in final_dict.keys():
        print(f"We have {final_dict[prod]} of {prod} left")
    else:
        print(f"Sorry, we don't have {prod}")