board = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", "X", "O"]
]

for row in board:
    print(" ".join(row))

print("\n" + "="*40 + "\n")


cells = input("Enter cells: ")

print("---------")

for i in range(0, 9, 3):
    row_str = cells[i:i + 3]
    print(f"| {row_str[0]} {row_str[1]} {row_str[2]} |")

print("---------")


x_count = cells.count('X')
o_count = cells.count('O') + cells.count('0')
empty_count = cells.count('_') + cells.count(' ')


winning_combinations = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]


x_wins = any(cells[a] == cells[b] == cells[c] == 'X' for a, b, c in winning_combinations)
o_wins = any(cells[a] == cells[b] == cells[c] in ('O', '0') for a, b, c in winning_combinations)


if abs(x_count - o_count) >= 2 or (x_wins and o_wins):
    print("Impossible")
elif x_wins:
    print("X wins")
elif o_wins:
    print("O wins")
elif empty_count > 0:
    print("Game not finished")
else:
    print("Draw")