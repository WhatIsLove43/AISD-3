def print_matrix(matrix, name):
    print(f"Матрица{name}:")
    for row in matrix:
        print(row)
    print()


def create_test_matrices(N):
#Создает тестовую матрицу A и разбивает ее на подматрицы B, C, D, E
    size = N // 2
    B = [[1 for _ in range(size)] for _ in range(size)]
    C = [[2 if (i + j) % 2 == 0 else 0 for j in range(size)] for i in range(size)]
    D = [[4 for _ in range(size)] for _ in range(size)]
    E = [[3 for _ in range(size)] for _ in range(size)]

    # Формируем A из B, C, D, E
    A = [[0] * N for _ in range(N)]
    for i in range(size):
        for j in range(size):
            A[i][j + size] = B[i][j]  # B
            A[i][j] = E[i][j]  # E
            A[i + size][j] = D[i][j]  # D
            A[i + size][j + size] = C[i][j]  # C
    return A, B, C, D, E


def count_zeros_in_odd_columns(matrix):
#Считает количество нулей в нечетных столбцах области 1 матрицы C
    size = len(matrix)
    count = 0
    for j in range(0, size, 2):  # Нечетные столбцы
        for i in range(j + 1):  # Область 1
            if matrix[i][j] == 0:
                count += 1
    return count


def perimeter_product_area4(matrix):
    #Вычисляет произведение чисел по периметру области 4
    size = len(matrix)
    product = 1
    for j in range(size):  # Верхний и нижний ряды
        product *= matrix[0][j] if matrix[0][j] != 0 else 1
        product *= matrix[size - 1][j] if matrix[size - 1][j] != 0 else 1
    for i in range(1, size - 1):  # Левые и правые столбцы
        product *= matrix[i][0] if matrix[i][0] != 0 else 1
        product *= matrix[i][size - 1] if matrix[i][size - 1] != 0 else 1
    return product


def swap_symmetric_area1_area3(matrix):
    #Меняет симметрично области 1 и 3 в матрице C
    size = len(matrix)
    for j in range(size // 2):
        for i in range(j + 1):
            matrix[i][j], matrix[size - 1 - i][size - 1 - j] = matrix[size - 1 - i][size - 1 - j], matrix[i][j]


def swap_matrices_non_symmetric(B, E):
    #Меняет матрицы B и E несимметрично
    size = len(B)
    for i in range(size):
        for j in range(size):
            B[i][j], E[i][j] = E[i][j], B[i][j]


def calculate_expression(K, A, F):
    #Вычисляет ((K * A^T) * (F + A - F))
    N = len(A)

    # Транспонирование A
    AT = [[A[j][i] for j in range(N)] for i in range(N)]

    # Умножение K * AT
    K_AT = [[K * AT[i][j] for j in range(N)] for i in range(N)]

    # Сложение F + A - F = A
    result_matrix = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result_matrix[i][j] = K_AT[i][j] * A[i][j]
    return result_matrix


def main():
    K = int(input("Введите значение K: "))
    N = int(input("Введите размер матрицы N (четное число): "))
    if N % 2 != 0:
        print("Размер матрицы должен быть четным.")
        return

    # Создаем матрицу A и подматрицы
    A, B, C, D, E = create_test_matrices(N)
    print_matrix(A, " A (исходная)")

    # Условие: сравниваем количество нулей и произведение
    zeros_count = count_zeros_in_odd_columns(C)
    perimeter_product = perimeter_product_area4(C)

    if zeros_count>perimeter_product:
        print("Меняем симметрично области 1 и 3 в C.")
        swap_symmetric_area1_area3(C)
    else:
        print("Меняем местами B и E несимметрично.")
        swap_matrices_non_symmetric(B, E)

    # Формируем матрицу F
    F, _, _, _, _ = create_test_matrices(N)
    print_matrix(F, "F (модифицированная)")

    # Вычисляем выражение
    result = calculate_expression(K, A, F)
    print_matrix(result, "Результат ((K * A^T) * (F + A - F))")

if __name__ == "__main__":
    main()
