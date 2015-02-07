a = int(input("Enter a: "))
b = int(input("Enter b: "))
oper = input("Enter operation: ")

if oper == "+":
    result = a + b
    print("Result is: " + str(result))
elif oper == "-":
    result = a - b
    print("Result is: " + str(result))
elif oper == "*":
    result = a * b
    print("Result is: " + str(result))
elif oper == "/":
    result = a / b
    print("Result is: " + str(result))
else:
    print("We do not support that operation.")