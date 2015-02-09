n = int(input("Enter n: "))
divider = 2
is_prime = True

while divider < n:
    if n % divider == 0:
        is_prime = False
        break
    divider += 1

print("{} is prime? {}".format(n, is_prime))