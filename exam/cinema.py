def find_row(cinema):
    min_count = len(cinema[0]) + 1
    row = 0

    for x in range(0, len(cinema)):
        empty_seats = 0
        for y in range(0,  len(cinema[x])):
            if cinema[x][y] == 0:
                empty_seats += 1

        if empty_seats < min_count and empty_seats != 0:
            min_count = empty_seats
            row = x + 1

    return row


def find_col(row, cinema):
    if 0 in cinema[row]:
        return cinema[row].index(0) + 1
    else:
        return -1


def order_of_seats(cinema):
    result_list = []

    while True:
        row = find_row(cinema)
        col = find_col(row - 1, cinema)

        if col != -1:
            result_list += [(row, col)]
            cinema[row - 1][col - 1] = 1
        else:
            break

    return result_list


print(order_of_seats([[1, 1, 1, 0], [1, 0, 1, 0], [0, 0, 0, 0]]))
print(order_of_seats([[1, 1, 1], [1, 0, 0], [1, 0, 0], [1, 1, 0]]))
print(order_of_seats([[0, 0], [0, 0], [0, 0]]))