n = int(input("Enter n: "))
tempN = n
newNumber = ""

while tempN > 0:
    newNumber += str(tempN % 10)
    tempN //= 10

if str(n) == newNumber:
    print("{} is palindrom".format(n))
else:
    print("{} is not palindrom".format(n))