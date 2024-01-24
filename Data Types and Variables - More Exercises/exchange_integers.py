number_a = int(input())
number_b = int(input())
tempvar_a = number_a

print("Before:")
print(f"a = {number_a}")
print(f"b = {number_b}")

number_a = number_b
number_b = tempvar_a

print("After:")
print(f"a = {number_a}")
print(f"b = {number_b}")
