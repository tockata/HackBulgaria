def square(x):
    return x ** 2


print(square(2))
print(square(5))

###########################
def fact(x):
    count = 1
    factoriel = 1
    while count <= x:
        factoriel *= count
        count += 1
    return factoriel


print(fact(5))
print(fact(0))
print(fact(6))

###########################
def count_elements(items):
    count = 0
    for element in items:
        count += 1
    return count


print(count_elements([]))
print(count_elements([1, 2, 3]))

###########################
def member(x, xs):
    for element in xs:
        if x == element:
            return True
    return False


print(member(1, [1, 2, 3]))
print(member("Python", ["Django", "Rails"]))

###########################
def grades_that_pass(students, grades, limit):
    result = []
    index = 0
    while index < len(students):
        if grades[index] >= limit:
            result += [students[index]]
        index += 1
    return result

students = ["Rado", "Ivo", "Maria", "Nina"]
grades = [3, 4.5, 5.5, 6]

result = grades_that_pass(students, grades, 4.0)
print(result)