n = int(input("Enter number n: "))
sumOfDigits = 0

while n > 0:
    sumOfDigits += n % 10
    n //= 10

print(sumOfDigits)