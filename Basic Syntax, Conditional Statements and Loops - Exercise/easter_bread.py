budget = float(input())
flour_price_per_kilo = float(input())
eggs_price = flour_price_per_kilo * 0.75
milk_price = (flour_price_per_kilo * 1.25) / 4
price_per_bread = flour_price_per_kilo + eggs_price + milk_price
number_of_loaves = 0
colored_eggs = 0
while budget > price_per_bread:
    number_of_loaves += 1
    colored_eggs += 3
    if number_of_loaves % 3 == 0:
        colored_eggs -= number_of_loaves - 2
    budget -= price_per_bread
print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")