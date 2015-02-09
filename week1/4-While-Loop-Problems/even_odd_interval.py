a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a > b:
    temp = a
    a = b
    b = temp

while a != b + 1:
    if a % 2 == 0:
        print(str(a) + " - even")
    else:
        print(str(a) + " - odd")
    a += 1