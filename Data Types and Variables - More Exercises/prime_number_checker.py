number = int(input())

its_prime = True
for current_number in range(2, number):
    if number % current_number == 0:
        its_prime = False

print(its_prime)