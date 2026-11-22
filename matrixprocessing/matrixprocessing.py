import math


def read_matrix(size_prompt, data_prompt):
    """Зчитує розміри матриці (n, m) та n рядків чисел з плаваючою комою."""
    n, m = map(int, input(size_prompt).split())
    print(data_prompt)
    matrix = []
    for _ in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)
    return n, m, matrix


def add_matrices(n1, m1, mat_a, n2, m2, mat_b):
    """Повертає суму двох матриць або None, якщо розмірності не збігаються."""
    if n1 != n2 or m1 != m2:
        return None

    return [
        [mat_a[i][j] + mat_b[i][j] for j in range(m1)]
        for i in range(n1)
    ]


def multiply_by_constant(n, m, matrix, scalar):
    """Множить кожен елемент матриці на константу (float)."""
    return [
        [matrix[i][j] * scalar for j in range(m)]
        for i in range(n)
    ]


def multiply_matrices(n1, m1, mat_a, n2, m2, mat_b):
    """Перемножує матрицю A (n1 x m1) на матрицю B (n2 x m2)."""
    if m1 != n2:
        return None

    result = []
    for i in range(n1):
        row = []
        for j in range(m2):
            value = 0.0
            for k in range(m1):
                value += mat_a[i][k] * mat_b[k][j]
            row.append(value)
        result.append(row)
    return result


def transpose_main_diagonal(n, m, matrix):
    """Транспонування матриці щодо головної діагоналі."""
    return [
        [matrix[i][j] for i in range(n)]
        for j in range(m)
    ]


def transpose_side_diagonal(n, m, matrix):
    """Транспонування матриці щодо побічної діагоналі."""
    return [
        [matrix[n - 1 - i][m - 1 - j] for i in range(n)]
        for j in range(m)
    ]


def transpose_vertical_line(n, m, matrix):
    """Транспонування матриці щодо вертикальної лінії."""
    return [
        [matrix[i][m - 1 - j] for j in range(m)]
        for i in range(n)
    ]


def transpose_horizontal_line(n, m, matrix):
    """Транспонування матриці щодо горизонтальної лінії."""
    return [
        [matrix[n - 1 - i][j] for j in range(m)]
        for i in range(n)
    ]


def transpose_matrix(n, m, matrix, mode):
    """Виконує обраний тип транспонування (1..4)."""
    if mode == "1":
        return transpose_main_diagonal(n, m, matrix)
    if mode == "2":
        return transpose_side_diagonal(n, m, matrix)
    if mode == "3":
        return transpose_vertical_line(n, m, matrix)
    if mode == "4":
        return transpose_horizontal_line(n, m, matrix)
    return None


def get_minor(matrix, row_to_remove, col_to_remove):
    """Повертає мінор (підматрицю) після викреслення заданого рядка та стовпця."""
    return [
        [
            matrix[i][j]
            for j in range(len(matrix[i]))
            if j != col_to_remove
        ]
        for i in range(len(matrix))
        if i != row_to_remove
    ]


def determinant(matrix):
    """Рекурсивно обчислює визначник квадратної матриці."""
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0.0
    for col in range(size):
        if matrix[0][col] == 0:
            continue
        sign = 1.0 if col % 2 == 0 else -1.0
        minor = get_minor(matrix, 0, col)
        det += sign * matrix[0][col] * determinant(minor)
    return det


def calculate_determinant(n, m, matrix):
    """Перевіряє, чи матриця квадратна, і повертає її визначник або None."""
    if n != m or n == 0:
        return None
    return determinant(matrix)


def inverse_matrix(n, m, matrix):
    """Обчислює зворотну матрицю або повертає None, якщо вона не існує."""
    if n != m or n == 0:
        return None

    det = determinant(matrix)
    if abs(det) < 1e-12:
        return None

    if n == 1:
        return [[1.0 / matrix[0][0]]]

    cofactors = []
    for i in range(n):
        row = []
        for j in range(n):
            sign = 1.0 if (i + j) % 2 == 0 else -1.0
            minor = get_minor(matrix, i, j)
            row.append(sign * determinant(minor))
        cofactors.append(row)

    adjugate = transpose_main_diagonal(n, n, cofactors)
    return [
        [adjugate[i][j] / det for j in range(n)]
        for i in range(n)
    ]


def format_number(num, truncate_two=False):
    """Форматує число для виводу (прибирає зайві нулі та захищає від -0)."""
    if abs(num) < 1e-12:
        num = 0.0

    if truncate_two:
        # Усічення до 2 знаків після коми (відповідає формату прикладу Етапу 6)
        truncated = math.trunc(num * 100) / 100.0
        if abs(truncated) < 1e-12:
            truncated = 0.0
        if truncated.is_integer():
            return str(int(truncated))
        text = f"{truncated:.2f}".rstrip("0").rstrip(".")
        return "0" if text in ("", "-0") else text

    if isinstance(num, float) and num.is_integer():
        return str(int(num))
    return str(num)


def print_matrix(matrix, truncate_two=False):
    """Виводить матрицю у форматі з прикладу."""
    print("The result is:")
    for row in matrix:
        print(" ".join(format_number(x, truncate_two=truncate_two) for x in row))


def print_scalar_result(value):
    """Виводить скалярний результат (наприклад, визначник)."""
    print("The result is:")
    print(format_number(value))


def print_menu():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")


def print_transpose_menu():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")


def main():
    while True:
        print_menu()
        choice = input("Your choice: ").strip()

        if choice == "0":
            break
        elif choice == "1":
            n1, m1, mat_a = read_matrix(
                "Enter size of first matrix: ", "Enter first matrix:"
            )
            n2, m2, mat_b = read_matrix(
                "Enter size of second matrix: ", "Enter second matrix:"
            )
            result = add_matrices(n1, m1, mat_a, n2, m2, mat_b)
            if result is None:
                print("The operation cannot be performed.")
            else:
                print_matrix(result)
        elif choice == "2":
            n, m, matrix = read_matrix(
                "Enter size of matrix: ", "Enter matrix:"
            )
            scalar = float(input("Enter constant: "))
            result = multiply_by_constant(n, m, matrix, scalar)
            print_matrix(result)
        elif choice == "3":
            n1, m1, mat_a = read_matrix(
                "Enter size of first matrix: ", "Enter first matrix:"
            )
            n2, m2, mat_b = read_matrix(
                "Enter size of second matrix: ", "Enter second matrix:"
            )
            result = multiply_matrices(n1, m1, mat_a, n2, m2, mat_b)
            if result is None:
                print("The operation cannot be performed.")
            else:
                print_matrix(result)
        elif choice == "4":
            print_transpose_menu()
            mode = input("Your choice: ").strip()
            n, m, matrix = read_matrix(
                "Enter matrix size: ", "Enter matrix:"
            )
            result = transpose_matrix(n, m, matrix, mode)
            if result is None:
                print("The operation cannot be performed.")
            else:
                print_matrix(result)
        elif choice == "5":
            n, m, matrix = read_matrix(
                "Enter matrix size: ", "Enter matrix:"
            )
            result = calculate_determinant(n, m, matrix)
            if result is None:
                print("The operation cannot be performed.")
            else:
                print_scalar_result(result)
        elif choice == "6":
            n, m, matrix = read_matrix(
                "Enter matrix size: ", "Enter matrix:"
            )
            result = inverse_matrix(n, m, matrix)
            if result is None:
                print("This matrix doesn't have an inverse.")
            else:
                print_matrix(result, truncate_two=True)


if __name__ == "__main__":
    main()

