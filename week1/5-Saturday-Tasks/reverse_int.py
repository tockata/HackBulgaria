n = int(input("Enter n: "))
newNumber = ""

while n > 0:
    newNumber += str(n % 10)
    n //= 10

print(newNumber)