n = input("Enter count of numbers: ")
n = int(n)

count = 1
numbers = []

while count <= n:
    number = input("Enter number: ")
    number = int(number)

    if number % 2 == 0:
        numbers = numbers + [number]

    count += 1

print("Count of evens: " + str(len(numbers)))
print("Evens are:")
for number in numbers:
    print(number)
