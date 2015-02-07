from random import randint

number = int(input("Enter sides: "))

first_roll = randint(1, number)
print("First roll:")
print(first_roll)

second_roll = randint(1, number)
print("Second roll:")
print(second_roll)

third_roll = randint(1, number)
print("Third roll:")
print(third_roll)

print("Sum is:")
print(first_roll + second_roll + third_roll)