def magic_square(square):
    sum_to_check = sum(square[0])
    length = len(square[0])

    for row in square:
        temp_sum = sum(row)
        if temp_sum != sum_to_check:
            return False

    temp_sum = 0
    for i in range(0, length):
        for j in range(0, length):
            temp_sum += square[i][j]

        if temp_sum != sum_to_check:
            return False
        temp_sum = 0

    temp_sum = 0
    for i in range(0, length):
        temp_sum += square[i][i]

    if temp_sum != sum_to_check:
            return False

    temp_sum = 0
    for i in range(length - 1, -1, -1):
        temp_sum += square[i][i]

    if temp_sum != sum_to_check:
            return False

    return True

square1 = [[23, 28, 21], [22, 24, 26], [27, 20, 25]]
square2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(magic_square(square1))
print(magic_square(square2))