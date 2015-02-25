def divisors(n):
    count = 1
    result = []
    while count <= n - 1:
        if n % count == 0:
            result += [count]
        count += 1
    return result

n = input("Enter n: ")
n = int(n)

print("Divisors of {} are {}".format(n, divisors(n)))