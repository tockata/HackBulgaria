n = int(input("Enter number n: "))
count = 1
sumOfEvenNumbers = 0

while count <= n:
    if count % 2 == 0:
        sumOfEvenNumbers += count
    count += 1

print(sumOfEvenNumbers)