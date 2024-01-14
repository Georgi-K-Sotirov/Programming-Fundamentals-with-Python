coffee_needed = 0
events_list_lower = ["coding", "dog", "cat", "movie"]
events_list_upper = ["CODING", "DOG", "CAT", "MOVIE"]

while True:
    events = input()
    if events in events_list_lower:
        coffee_needed += 1
    elif events in events_list_upper:
        coffee_needed += 2
    if events == "END":
        break
if coffee_needed <= 5:
    print(coffee_needed)
else:
    print("You need extra sleep")
