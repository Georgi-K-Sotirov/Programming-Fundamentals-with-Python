def multiplication_sign(x, y, z):

    if x == 0 or y == 0 or z == 0:
        return "zero"

    else:
        my_list = (x, y, z)
        negative_counter = 0
        for num in my_list:
            if num < 0:
                negative_counter += 1
        if negative_counter % 2 == 0:
            return "positive"
        else:
            return "negative"


x = int(input())
y = int(input())
z = int(input())

print(multiplication_sign(x, y, z))