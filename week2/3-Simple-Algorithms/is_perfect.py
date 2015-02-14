n = input("Enter n: ")
n = int(n)

count = 1
divisors = []
sum_of_divisors = 0
is_perfect = False

while count <= n - 1:
    if n % count == 0:
        divisors += [count]
        sum_of_divisors += count

    count += 1

if sum_of_divisors == n:
    is_perfect = True

print("Number {} with divisors {} is perfect? {}".format(n, divisors, is_perfect))