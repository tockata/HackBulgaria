def str_reverse(string):
    result = ""

    for i in range(len(string) -1, -1, -1):
        result += string[i]

    return result

print(str_reverse("Python"))
print(str_reverse("kapak"))
print(str_reverse(""))

def join(delimiter, items):
    result = ""

    for i in range(0, len(items)):
        if i == 0:
            result += items[i]
        else:
            result += delimiter + items[i]

    return result

print(join(" ", ["Radoslav", "Yordanov", "Georgiev"]))
print(join("\n", ["line1", "line2"]))
print()

def startswith(search, string):
    if search == string[0:len(search)]:
        return True

    return False

print(startswith("Py", "Python"))
print(startswith("py", "Python"))
print(startswith("baba", "asdbaba"))
print()

def endswith(search, string):
    if search == string[len(string) - len(search):len(string)]:
        return True

    return False

print(endswith(".py", "hello.py"))
print(endswith("kapak", "babakapak"))
print(endswith(" ", "Python   "))
print(endswith("py", "python"))
print()

def trim(string):
    return string.strip(" ")

print(trim("   asda   "))
print(trim(" spacious    "))
print(trim("no here but yes at end   "))
print(trim("                      "))
print(trim("python"))