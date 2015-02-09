n = int(input("Enter three digit number n: "))
first_digit = n % 10
n //= 10
second_digit = n % 10
n //= 10
third_digit = n % 10

first_number = str(first_digit) + str(second_digit) + str(third_digit)
second_number = str(second_digit) + str(first_digit) + str(third_digit)
third_number = str(second_digit) + str(third_digit) + str(first_digit)
fourth_number = str(third_digit) + str(first_digit) + str(second_digit)
fifth_number = str(third_digit) + str(second_digit) + str(first_digit)

max_number = first_number
min_number = first_number
if second_number > max_number:
    max_number = second_number
if third_number > max_number:
    max_number = third_number
if third_number > max_number:
    max_number = third_number
if fourth_number > max_number:
    max_number = fourth_number
if fifth_number > max_number:
    max_number = fifth_number

if second_number < max_number:
    max_number = second_number
if third_number < max_number:
    max_number = third_number
if third_number < max_number:
    max_number = third_number
if fourth_number < max_number:
    max_number = fourth_number
if fifth_number < max_number:
    max_number = fifth_number

print(max_number)
print(min_number)