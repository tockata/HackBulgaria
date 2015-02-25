def divisors(n):
    count = 1
    result = []
    while count <= n - 1:
        if n % count == 0:
            result += [count]
        count += 1
    return result

def sum_ints(numbers):
    sum_of_ints = 0
    for integer in numbers:
        sum_of_ints += integer
    return sum_of_ints

def is_perfect(n):
    return n == sum_ints(divisors(n))

n = input("Enter n: ")
n = int(n)

number = 2
perfect_numbers = []
outer_count = len(perfect_numbers)

while outer_count < n:
    if is_perfect(number):
        perfect_numbers += [number]

    number += 1
    outer_count = len(perfect_numbers)

print("First {} perfect numbers are: {}".format(n, perfect_numbers))
