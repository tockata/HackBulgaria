n = int(input("Enter number n: "))
count = 1
sumOfOddNumbers = 0

while count <= n:
    if count % 2 != 0:
        sumOfOddNumbers += count
    count += 1

print(sumOfOddNumbers)