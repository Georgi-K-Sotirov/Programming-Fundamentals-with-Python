number = int(input())
list_numer =[]

for digit in str(number):
    list_numer += digit

list_numer.sort(reverse=True)
for i in list_numer:
    print(i, end="")
