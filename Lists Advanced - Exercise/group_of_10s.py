number_sequence = [int(num) for num in input().split(", ")]
group = 10

while number_sequence:
    current_group = [num for num in number_sequence if num <= group]
    number_sequence = [num for num in number_sequence if num not in current_group]
    print(f"Group of {group}'s: {current_group}")
    group += 10