number = int(input())
positive = []
negative = []



for i in range(number):
    data = int(input())
    if data < 0:
        negative.append(data)
    else:
        positive.append(data)

count_positives = len(positive)
sum_of_negatives = sum(negative)

print(positive)
print(negative)
print(f'Count of positives: {count_positives}')
print(f'Sum of negatives: {sum_of_negatives}')