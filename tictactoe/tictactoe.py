
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

# Виводимо нижню межу ігрового поля
print("---------")