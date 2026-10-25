board = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", "X", "O"]
]

for row in board:
    print(" ".join(row))

print("\n" + "=" * 40 + "\n")

# Етап 2: Зчитування рядка та виведення динамічної сітки
cells = input("Enter cells: ")

print("---------")

for i in range(0, 9, 3):
    row_str = cells[i:i + 3]
    print(f"| {row_str[0]} {row_str[1]} {row_str[2]} |")

print("---------")

# Етап 3: Аналіз стану гри
x_count = cells.count('X')
o_count = cells.count('O') + cells.count('0')
empty_count = cells.count('_') + cells.count(' ')

winning_combinations = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Рядки
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Стовпчики
    (0, 4, 8), (2, 4, 6)  # Діагоналі
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

print("\n" + "=" * 40 + "\n")

# Етап 4: Інтерактивний хід гравця (X) та оновлення поля
# Оскільки рядки в Python незмінні, перетворюємо cells у список
cells_list = list(cells)

while True:
    user_input = input("Enter the coordinates: ").split()

    # Перевіряємо, чи введено рівно два значення
    if len(user_input) != 2:
        print("You should enter numbers!")
        continue

    # Перевіряємо, чи є введені значення числами
    try:
        row = int(user_input[0])
        col = int(user_input[1])
    except ValueError:
        print("You should enter numbers!")
        continue

    # Перевіряємо, чи знаходяться координати в межах від 1 до 3
    if not (1 <= row <= 3 and 1 <= col <= 3):
        print("Coordinates should be from 1 to 3!")
        continue

    # Обчислюємо індекс у списку за координатами
    index = (row - 1) * 3 + (col - 1)

    # Перевіряємо, чи комірка порожня
    if cells_list[index] not in ('_', ' '):
        print("This cell is occupied! Choose another one!")
        continue

    # Ставимо 'X' у відповідну клітинку та виходимо з циклу
    cells_list[index] = 'X'
    break

# Виводимо оновлену ігрову сітку після успішного ходу
print("---------")
for i in range(0, 9, 3):
    print(f"| {cells_list[i]} {cells_list[i + 1]} {cells_list[i + 2]} |")
print("---------")