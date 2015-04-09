def second_largest(numbers):
    if len(numbers) < 2:
        print(False)
        return

    sorted_numbers = sorted(numbers)
    index = len(sorted_numbers) - 1

    while index > 0:
        if sorted_numbers[index] != sorted_numbers[index - 1]:
            print(sorted_numbers[index - 1])
            return

        index -= 1

    print(False)
    return


second_largest([])
second_largest([2, 1])
second_largest([5, 5])
second_largest([100, 100, 90])
second_largest([4, 5, 13, 50, -50, -10])
