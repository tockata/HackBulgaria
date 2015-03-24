n = 0
while n % 2 == 0:
    n = int(input("Enter odd number: "))

boundaries = 0
sand_watch = n
result = ""

for i in range(0, n):
    b = "." * boundaries
    s = "*" * sand_watch
    result += b + s + b + "\n"

    if i < (n / 2 - 1):
        boundaries += 1
        sand_watch -= 2
    else:
        boundaries -= 1
        sand_watch += 2

print(result)