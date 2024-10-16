import random

def create_board():
    board = [[0] * 9 for _ in range(9)]
    for _ in range(17):  # Minimum number of clues
        row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
        while not valid(board, row, col, num) or board[row][col] != 0:
            row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
        board[row][col] = num
    return board
def valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row//3), 3 * (col//3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(" ".join(str(num) if num != 0 else '.' for num in row[j:j+3]) for j in range(0, 9, 3)))
        if (i + 1) % 3 == 0 and i != 8:
            print("-" * 21)

def main():
    board = create_board()
    print_board(board)
main()
