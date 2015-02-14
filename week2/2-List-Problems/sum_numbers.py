n = input("Enter count of numbers: ")
n = int(n)

count = 1
numbers = []
sum_of_numbers = 0

while count <= n:
    number = input("Enter number: ")
    number = int(number)
    numbers += [number]
    sum_of_numbers += number

    count += 1

print("Sum of numbers: {} is {}".format(numbers, sum_of_numbers))