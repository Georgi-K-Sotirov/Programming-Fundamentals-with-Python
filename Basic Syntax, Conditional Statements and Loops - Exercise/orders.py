numbers_of_order = int(input())
total_price = 0
for _ in range(numbers_of_order):
    price_per_capsule = float(input())
    number_of_days = int(input())
    capsules_per_day = int(input())

    if not 0.01 <= price_per_capsule <= 100:
        continue
    elif not 1<= number_of_days <= 31:
        continue
    elif not 1 <= capsules_per_day <= 2000:
        continue
    price = price_per_capsule * capsules_per_day * number_of_days
    print(f"The price for the coffee is: ${price:.2f}")
    total_price += price

print(f"Total: ${total_price:.2f}")
