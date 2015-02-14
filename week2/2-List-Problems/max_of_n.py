n = input("Enter count of numbers: ")
n = int(n)

count = 1
numbers = []

while count <= n:
    number = input("Enter number: ")
    number = int(number)
    numbers += [number]

    count += 1

greatest_number = numbers[0]
for number in numbers:
    if number > greatest_number:
        greatest_number = number

print("Greatest number from: {} is {}".format(numbers, greatest_number))
