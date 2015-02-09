a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a > b:
    temp = a
    a = b
    b = temp

while a != b + 1:
    print(a)
    a += 1
