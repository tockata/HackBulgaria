def is_string_palindrom(string):
    punktuation_marks = ["!", "?", ".", ","]
    string = string.replace(" ", "")
    string = string.lower()

    for i in range(0, len(punktuation_marks)):
        string = string.replace(punktuation_marks[i], "")

    reversed_string = string[::-1]

    return string == reversed_string

print(is_string_palindrom("Az obi4am ma4 i boza"))
print(is_string_palindrom("A Toyota!"))
print(is_string_palindrom("bozaaa"))
print(is_string_palindrom(" kapak! "))