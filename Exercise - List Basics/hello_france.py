collection_of_items = input().split("|")
budget = float(input())
ticket_price = 150
buy_items = []
sell_items = []

for current_collection in collection_of_items:
    current_collection_as_list = current_collection.split("->")
    current_item = current_collection_as_list[0]
    current_price = float(current_collection_as_list[1])
    if current_item == "Clothes":
        if budget >= current_price and current_price <= 50:
            budget -= current_price
            buy_items.append(current_price)
            sell_items.append(current_price * 1.40)
    elif current_item == "Shoes":
        if budget >= current_price and current_price <= 35:
            budget -= current_price
            buy_items.append(current_price)
            sell_items.append(current_price * 1.40)
    elif current_item == "Accessories":
        if budget >= current_price and current_price <= 20.50:
            budget -= current_price
            buy_items.append(current_price)
            sell_items.append(current_price * 1.40)
profit = sum(sell_items) - sum(buy_items)
print(" ".join(map(str, ('{:.2f}'.format(f) for f in sell_items))))
print(f"Profit: {profit:.2f}")
if budget + sum(sell_items) >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")
