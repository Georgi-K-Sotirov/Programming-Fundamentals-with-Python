from math import floor


def line_length(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def center_point(x1, y1, x2, y2):
    distance1 = (x1 ** 2 + y1 ** 2) ** 0.5
    distance2 = (x2 ** 2 + y2 ** 2) ** 0.5

    if distance1 <= distance2:
        return f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})"
    else:
        return f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())


first_line = line_length(x1, y1, x2, y2)
second_line = line_length(x3, y3, x4, y4)

if first_line >= second_line:
    print(center_point(x1, y1, x2, y2))
else:
    print(center_point(x3, y3, x4, y4))