n = int(input("Enter number n: "))
m = int(input("Enter number m: "))

if n % 10 > m % 10:
    print(n)
elif n % 10 < m % 10:
    print(m)
else:
    if n > m:
        print(n)
    elif n < m:
        print(m)
    else:
        print("n is equal to m")