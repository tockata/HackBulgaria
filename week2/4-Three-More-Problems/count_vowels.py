string = input("Enter string: ")
vowels = "aeiouyAEIOUY"

string_as_list = list(string)
count = 0

for character in string_as_list:
    if character in vowels:
        count += 1

print(count)