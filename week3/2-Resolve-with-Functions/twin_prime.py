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

p = input("Enter p: ")
p = int(p)

q1 = p - 2
q2 = p + 2

numbers = [q1, p, q2]
prime_checks = []

for number in numbers:
    prime_checks += [is_prime(number)]

if False not in prime_checks:
    print("Twins: {} and {}".format(str(numbers[0]), str(numbers[1])))
    print("Twins: {} and {}".format(str(numbers[1]), str(numbers[2])))
elif prime_checks[0] == True and prime_checks[1] == True:
    print("Twins: {} and {}".format(str(numbers[0]), str(numbers[1])))
elif prime_checks[1] == True and prime_checks[2] == True:
    print("Twins: {} and {}".format(str(numbers[1]), str(numbers[2])))
else:
    print("No twins!")