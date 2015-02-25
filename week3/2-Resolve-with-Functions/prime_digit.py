def to_digits(n):
    digits = []
    while n > 0:
        digit = n % 10
        digits += [digit]
        n //= 10
    return digits

def is_prime(n):
    if n < 2:
        return False

    count = 2
    if n > 2:
        while count <= n - 1:
            if n % count == 0:
                return False
            count += 1
    return True

n = input("Enter n: ")
n = int(n)

digits = to_digits(n)

found_prime_digit = False

for digit in digits:
    if is_prime(digit):
        found_prime_digit = True

if found_prime_digit:
    print("Number {} contains prime digit".format(n))
else:
    print("Number {} does not contain prime digit".format(n))