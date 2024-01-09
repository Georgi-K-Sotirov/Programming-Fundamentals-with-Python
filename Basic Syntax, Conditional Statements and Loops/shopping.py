budget = int(input())

number = input()
while number != "End":
    number = int(number)
    budget -= number
    if budget < 0:
        print("You went in overdraft!")
        break
    number = input()
else:
    print("You bought everything needed.")
