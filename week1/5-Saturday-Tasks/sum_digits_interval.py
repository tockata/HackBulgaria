n = int(input("Enter number n: "))
m = int(input("Enter number m: "))

while n <= m:
    tempNumber = n
    sumOfDigits = 0
    while tempNumber > 0:
        sumOfDigits += tempNumber % 10
        tempNumber //= 10
    print("Sum of digits of {} = {}".format(n, sumOfDigits))
    n += 1