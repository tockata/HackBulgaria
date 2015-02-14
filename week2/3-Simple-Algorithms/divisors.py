n = input("Enter n: ")
n = int(n)

count = 1
divisors = []

while count <= n - 1:
    if n % count == 0:
        divisors += [count]

    count += 1

print("Divisors of {} are {}".format(n, divisors))