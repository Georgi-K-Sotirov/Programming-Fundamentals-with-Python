words = input().lower().split()
my_dict = {}

for word in words:
    if word not in my_dict.keys():
        my_dict[word] = 0
    my_dict[word] += 1

for key in my_dict.keys():
    if my_dict[key] % 2 != 0:
        print(key, end=" ")