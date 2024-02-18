def total_price(product, qty):
    if product == "coffee":
        return qty * 1.5
    elif product == "coke":
        return qty * 1.4
    elif product == "water":
        return  qty * 1
    elif product == "snacks":
        return qty * 2


product = input()
qty = int(input())

print(f"{total_price(product, qty):.2f}")