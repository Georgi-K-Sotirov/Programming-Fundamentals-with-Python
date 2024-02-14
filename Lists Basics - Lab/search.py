number = int(input())
key_word = input()

ins_list = []
for _ in range(number):
    data = input()
    ins_list.append(data)

filter_list = []

for i in range(len(ins_list)):
    if key_word in ins_list[i]:
        filter_list.append(ins_list[i])

print(ins_list)
print(filter_list)