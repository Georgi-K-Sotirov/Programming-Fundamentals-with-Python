number = int(input())

last_bracket = ")"
for index in range(number):
    current_bracket = input()
    if current_bracket == "(" or current_bracket == ")":
        if current_bracket == last_bracket:
            print("UNBALANCED")
            break
        last_bracket = current_bracket
else:
    if last_bracket != ")":
        print("UNBALANCED")
    else:
        print("BALANCED")