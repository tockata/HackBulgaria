def prime_pair(numbers):
    for n1 in numbers:
        for n2 in numbers:
            numberToCheck = n1 + n2
            if numberToCheck < 2:
                return False

            start = 2
            is_prime = True

            while start < numberToCheck:
                if numberToCheck % start == 0:
                    is_prime = False
                    break

                start += 1

            return is_prime

print(prime_pair([1, 2, 3, 4, 5]))