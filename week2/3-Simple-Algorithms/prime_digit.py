n = input("Enter n: ")
n = int(n)

digits = []
prime_number_found = False

while n > 0:
    digit = n % 10
    digits += [digit]
    n //= 10

for digit in digits:
    count = 2
    is_prime = True

    if digit > 2:
        while count <= digit - 1:
            if digit % count == 0:
                is_prime = False
                break
            count += 1

        if is_prime == True:
            prime_number_found = True
            print("Yes")
            break

if prime_number_found == False:
    print("No")