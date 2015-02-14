n = input("Enter n: ")
n = int(n)

number = 2
perfect_numbers = []
outer_count = len(perfect_numbers)

while outer_count < n:
    inner_count = 1
    divisors = []
    sum_of_divisors = 0

    while inner_count <= number - 1:
        if number % inner_count == 0:
            divisors += [inner_count]
            sum_of_divisors += inner_count

        inner_count += 1

    if sum_of_divisors == number:
        perfect_numbers += [number]

    number += 1
    outer_count = len(perfect_numbers)

print("First {} perfect numbers are: {}".format(n, perfect_numbers))
