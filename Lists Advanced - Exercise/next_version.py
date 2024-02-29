version = [int(num) for num in input().split(".")]
version[-1] += 1

for current_index in range(len(version) - 1, 0, -1):
    if version[current_index] >= 10:
        version[current_index] -= 10
        version[current_index - 1] += 1

print(".".join(map(str, version)))