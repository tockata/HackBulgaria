n = 0
while n % 2 == 0:
    n = int(input("Enter odd number: "))

boundaries = 0
sand_clock = n
result = ""

for i in range(0, n):
    b = "." * boundaries
    s = "*" * sand_clock
    result += b + s + b + "\n"

    if i < (n / 2 - 1):
        boundaries += 1
        sand_clock -= 2
    else:
        boundaries -= 1
        sand_clock += 2

print(result)