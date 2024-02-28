def tribonacci_sequence(num):
    result = []
    for digit in range(num):
        if len(result) < 2:
            result.append(1)
        else:
            result.append(sum(result[-1:-4:-1]))
    return map(str, result)


num = int(input())
print(" ".join(tribonacci_sequence(num)))