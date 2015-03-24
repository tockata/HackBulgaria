def taken_name(surname_husband, surname_wife):
    surname_wife_substring = \
        surname_wife[len(surname_wife) - len(surname_husband) - 1: len(surname_wife) - 1]
    return surname_husband == surname_wife_substring

print(taken_name("Petrov", "Petrova"))
print(taken_name("Ivanov", "Tsvetanova"))
print(taken_name("Petrov", "Ivanova-Petrova"))
