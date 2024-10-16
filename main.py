import random
board = [[0] * 9 for _ in range(9)]

for _ in range(17):  # Minimum number of clues
    row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
    board[row][col] = num

for i, row in enumerate(board):
    print(" | ".join(" ".join(str(num) if num != 0 else '.' for num in row[j:j+3]) for j in range(0, 9, 3)))
    if (i + 1) % 3 == 0 and i != 8:
        print("-" * 21)


