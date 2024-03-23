#В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в 2 раза.

def increase_non_diagonal(matrix):
    # Вывод исходной матрицы
    print("Исходная матрица:")
    for row in matrix:
        print(row)

    # Увеличение элементов не лежащих на главной диагонали
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j:
                matrix[i][j] *= 2

    # Вывод измененной матрицы
    print("\n Измененная матрица:")
    for row in matrix:
        print(row)

# Пример использования функции
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
increase_non_diagonal(matrix)
