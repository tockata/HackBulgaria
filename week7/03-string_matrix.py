def string_matrix(matrix_width, strings):
    result = ""

    for i in range(0, matrix_width):
        result += "|"
        for j in range(0, matrix_width):
            if j < len(strings[i]):
                result += " " + strings[i][j] + " |"
            else:
                result += " X |"
        result += "\n"

    return result

print(string_matrix(6,["python","gogo","perl","java","haskell","ruby0nRails"]))