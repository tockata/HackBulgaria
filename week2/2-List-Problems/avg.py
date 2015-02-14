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

avg = sum_of_numbers / len(numbers)
print("Avg of numbers: {} is {}".format(numbers, avg))