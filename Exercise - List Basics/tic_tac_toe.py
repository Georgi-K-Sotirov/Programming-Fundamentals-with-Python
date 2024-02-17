first_row = [int(x) for x in input().split(" ")]
second_row = [int(x) for x in input().split(" ")]
third_row = [int(x) for x in input().split(" ")]

win = False
winner = 0

if first_row[0] == first_row[1] and first_row[1] == first_row[2]:
    win = True
    winner = first_row[0]
elif second_row[0] == second_row[1] and second_row[1] == second_row[2]:
    win = True
    winner = second_row[0]
elif third_row[0] == third_row[1] and third_row[1] == third_row[2]:
    win = True
    winner = third_row[0]
for colum in range(len(first_row)):
    if first_row[colum] == second_row[colum] and second_row[colum] == third_row[colum]:
        win = True
        winner = first_row[colum]
if first_row[0] == second_row[1] and second_row[1] == third_row[2]:
    win = True
    winner = first_row[0]
elif first_row[2] == second_row[1] and second_row[1] == third_row[0]:
    win = True
    winner = first_row[2]

if win:
    if winner == 1:
        print("First player won")
    elif winner == 2:
        print("Second player won")
    if winner == 0:
        print("Draw!")
else:
    print("Draw!")