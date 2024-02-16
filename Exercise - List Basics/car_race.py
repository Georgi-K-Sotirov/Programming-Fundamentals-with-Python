race = [int(i) for i in input().split(" ")]
first_car_time = 0
second_car_time = 0

first_car_track = race[:len(race)//2:]
second_car_track = race[len(race)//2+1::]
second_car_track.reverse()

for time in first_car_track:
    if time == 0:
        first_car_time *= 0.8
    first_car_time += time

for time in second_car_track:
    if time == 0:
        second_car_time *= 0.8
    second_car_time += time

if first_car_time < second_car_time:
    print(f"The winner is left with total time: {first_car_time:.1f}")
elif first_car_time > second_car_time:
    print(f"The winner is right with total time: {second_car_time:.1f}")