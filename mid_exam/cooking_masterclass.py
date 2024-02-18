from math import ceil

budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())

flour_qty = students - (students // 5)
egg_qty = students * 10
apron_qty = ceil(students * 1.2)

total_price = flour_qty * flour_price + egg_price * egg_qty + apron_qty * apron_price
diff = abs(total_price - budget)
if total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    print(f"{diff:.2f}$ more needed.")