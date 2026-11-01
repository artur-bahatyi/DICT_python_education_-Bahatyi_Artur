# Part 1: Initial Board State Analysis
board = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", "X", "O"]
]

for row in board:
    print(" ".join(row))

print("\n" + "=" * 40 + "\n")

# Standardizing input: convert any '_' to a space for consistency
cells = input("Enter cells: ").replace('_', ' ')

print("---------")

for i in range(0, 9, 3):
    row_str = cells[i:i + 3]
    print(f"| {row_str[0]} {row_str[1]} {row_str[2]} |")

print("---------")

x_count = cells.count('X')
o_count = cells.count('O')
empty_count = cells.count(' ')

winning_combinations = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]

x_wins = any(cells[a] == cells[b] == cells[c] == 'X' for a, b, c in winning_combinations)
o_wins = any(cells[a] == cells[b] == cells[c] == 'O' for a, b, c in winning_combinations)

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

print("\n" + "=" * 40 + "\n")

# Part 2: Single Move Placement
cells_list = list(cells)

while True:
    user_input = input("Enter the coordinates: ").split()

    if len(user_input) != 2:
        print("You should enter numbers!")
        continue

    try:
        row = int(user_input[0])
        col = int(user_input[1])
    except ValueError:
        print("You should enter numbers!")
        continue

    if not (1 <= row <= 3 and 1 <= col <= 3):
        print("Coordinates should be from 1 to 3!")
        continue

    index = (row - 1) * 3 + (col - 1)

    if cells_list[index] != ' ':
        print("This cell is occupied! Choose another one!")
        continue

    cells_list[index] = 'X'
    break

print("---------")
for i in range(0, 9, 3):
    print(f"| {cells_list[i]} {cells_list[i + 1]} {cells_list[i + 2]} |")
print("---------")

print("\n" + "=" * 40 + "\n")

# Part 3: Interactive Two-Player Game Loop
game_cells = [' '] * 9
current_player = 'X'

while True:
    print("---------")
    for i in range(0, 9, 3):
        print(f"| {game_cells[i]} {game_cells[i + 1]} {game_cells[i + 2]} |")
    print("---------")

    x_wins_game = any(game_cells[a] == game_cells[b] == game_cells[c] == 'X' for a, b, c in winning_combinations)
    o_wins_game = any(game_cells[a] == game_cells[b] == game_cells[c] == 'O' for a, b, c in winning_combinations)
    empty_count_game = game_cells.count(' ')

    if x_wins_game:
        print("X wins")
        break
    elif o_wins_game:
        print("O wins")
        break
    elif empty_count_game == 0:
        print("Draw")
        break

    while True:
        user_input = input("Enter the coordinates: ").split()

        if len(user_input) != 2:
            print("You should enter numbers!")
            continue

        try:
            row = int(user_input[0])
            col = int(user_input[1])
        except ValueError:
            print("You should enter numbers!")
            continue

        if not (1 <= row <= 3 and 1 <= col <= 3):
            print("Coordinates should be from 1 to 3!")
            continue

        index = (row - 1) * 3 + (col - 1)

        if game_cells[index] != ' ':
            print("This cell is occupied! Choose another one!")
            continue

        game_cells[index] = current_player
        break

    current_player = 'O' if current_player == 'X' else 'X'