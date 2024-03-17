n = int(input())
my_dict = {}
for _ in range(n):
    key = input()
    synonym = input()

    if key not in my_dict:
        my_dict[key] = []
    my_dict[key].append(synonym)

for key, value in my_dict.items():
    value_as_str = ", ".join(value)
    print(f"{key} - {value_as_str}")