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

print("Number {} with divisors {} is perfect? {}".format(n, divisors(n), is_perfect(n)))