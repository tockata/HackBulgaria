a = int(input("Enter the lower bound of the interval: "))
b = int(input("Enter the upper bound of the interval: "))

while b <= a:
    b = int(input("Upper bound must be greater than lower, please input new number: "))

while True:
    x = int(input("Enter number: "))
    if x == a:
        print("The number is equal to the lower bound of the interval")
    elif x == b:
        print("The number is equal to the upper bound of the interval")
    elif a < x and x < b:
        print("The number is in the interval")
    elif x < a:
        print("The number is outside the interval, x < a")
    else:
        print("The number is outside the interval, x > b")
    answer = input("Do you want to continue? y/n: ")
    if answer == "n":
        break