my_list = [int(x) for x in input().split(" ")]
number = int(input())
last_order = []
index = 0

while len(my_list) != 0:
    index = (index + number - 1) % len(my_list)
    last_person = my_list.pop(index)
    last_order.append(last_person)

result = ",".join(map(str, last_order))
print("[" + result + "]")
