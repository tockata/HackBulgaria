def second_largest(numbers):
    if len(numbers) < 2:
        return False

    sorted_numbers = sorted(numbers)
    index = len(sorted_numbers) - 1

    while index > 0:
        if sorted_numbers[index] != sorted_numbers[index - 1]:
            return sorted_numbers[index - 1]

        index -= 1

    return False


print(second_largest([]))
print(second_largest([2, 1]))
print(second_largest([5, 5]))
print(second_largest([100, 100, 90]))
print(second_largest([4, 5, 13, 50, -50, -10]))
