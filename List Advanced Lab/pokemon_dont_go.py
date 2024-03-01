distance = [int(num) for num in input().split()]
total_sum = 0

while distance:
    index = int(input())
    if index < 0:
        index = 0
        removed_element = distance[index]
        distance[0] = distance[-1]
        total_sum += removed_element
        distance = [num + removed_element if num <= removed_element else num - removed_element for num in distance ]
    elif index >= len(distance):
        index = -1
        removed_element = distance[index]
        distance[-1] = distance[0]
        total_sum += removed_element
        distance = [num + removed_element if num <= removed_element else num - removed_element for num in distance]
    else:
        removed_element = distance.pop(index)
        total_sum += removed_element
        distance = [num + removed_element if num <= removed_element else num - removed_element for num in distance]

print(total_sum)