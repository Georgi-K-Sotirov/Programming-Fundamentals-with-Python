input_list = list(map(int, input().split()))
factor = int(input())

multiply_happiness = [x * factor for x in input_list]
happy_count = [x for x in multiply_happiness if x >= (sum(multiply_happiness)/len(multiply_happiness))]

if len(happy_count) >= len(multiply_happiness)/2:
    print(f'Score: {len(happy_count)}/{len(multiply_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(happy_count)}/{len(multiply_happiness)}. Employees are not happy!')