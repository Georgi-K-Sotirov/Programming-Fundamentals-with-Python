from math import floor


def center_point(x1, y1, x2, y2):
    distance1 = (x1 ** 2 + y1 ** 2) ** 0.5
    distance2 = (x2 ** 2 + y2 ** 2) ** 0.5

    if distance1 <= distance2:
        return f"({floor(x1)}, {floor(y1)})"
    else:
        return f"({floor(x2)}, {floor(y2)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(center_point(x1, y1, x2, y2))