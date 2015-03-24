def inner_trim(string):
    result = ' '.join(string.split())

    return result

print(inner_trim("Python    Django"))
print(inner_trim("  Python     Django   "))