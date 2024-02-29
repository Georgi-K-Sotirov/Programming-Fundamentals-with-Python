rooms = int(input())
total_people = 0
total_chairs = 0
for room in range(1, rooms +1 ):
    chairs, people = input().split()
    people = int(people)
    total_chairs += len(chairs)
    total_people += people
    diff = len(chairs) - people
    if len(chairs) < people:
        print(f"{abs(diff)} more chairs needed in room {room}")

if total_people <= total_chairs:
    print(f"Game On, {total_chairs - total_people} free chairs left")