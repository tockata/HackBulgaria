def board_to_string(board):
    result = ""

    for i in range(0, len(board)):
        result += "| " + board[i][0] + " | " + board[i][1] + " | " + board[i][2] + " |\n"

    return result


board = [ ["X", "O", "#"],
          ["X", "X", "X"],
          ["#", "#", "#"] ]

print(board_to_string(board))