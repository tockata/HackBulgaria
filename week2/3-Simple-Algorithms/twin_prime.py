p = input("Enter p: ")
p = int(p)

q1 = p - 2
q2 = p + 2

numbers = [q1, p, q2]
prime_checks = []

for number in numbers:
    count = 2
    is_prime = True

    if number > 2:
        while count <= number - 1:
            if number % count == 0:
                is_prime = False
                break
            count += 1

        if is_prime == True:
            prime_checks += [True]
        else:
            prime_checks += [False]

if False not in prime_checks:
    print("Twins: {} and {}".format(str(numbers[0]), str(numbers[1])))
    print("Twins: {} and {}".format(str(numbers[1]), str(numbers[2])))
elif prime_checks[0] == True and prime_checks[1] == True:
    print("Twins: {} and {}".format(str(numbers[0]), str(numbers[1])))
elif prime_checks[1] == True and prime_checks[2] == True:
    print("Twins: {} and {}".format(str(numbers[1]), str(numbers[2])))
else:
    print("No twins!")