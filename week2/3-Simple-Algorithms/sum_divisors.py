n = input("Enter n: ")
n = int(n)

count = 1
divisors = []
sum_of_divisors = 0

while count <= n - 1:
    if n % count == 0:
        divisors += [count]
        sum_of_divisors += count

    count += 1

print("Sum of divisors {} is: {}".format(divisors, sum_of_divisors))
