a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a > b:
    print("a({}) is bigger than b({})!".format(a, b))
elif a < b:
    print("b({}) is bigger than a({})!".format(b, a))
else:
    print("a({}) is equal to b({})!".format(a, b))