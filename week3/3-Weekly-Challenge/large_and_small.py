def to_digits(n):
    digits = []
    while n > 0:
        digit = n % 10
        digits += [digit]
        n //= 10
    return digits

def to_number(digits):
    string_of_digit = ""
    for digit in digits:
        string_of_digit += str(digit)
    return int(string_of_digit)

def find_max_number(digits):
    digits = sorted(digits, reverse=True)
    return digits

def find_min_number(digits):
    digits = sorted(digits)
    return digits

n = input("Enter number: ")
n = int(n)

digits = to_digits(n)

print(to_number(find_max_number(digits)))
print(to_number(find_min_number(digits)))