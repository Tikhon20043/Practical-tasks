#1. Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.

# импортируем модуль random для генерации случайных чисел
import random

# определяем размеры матрицы
rows = 3
cols = 3

# создаем пустую матрицу
matrix = []

# генерируем случайные числа и заполняем матрицу
for i in range(rows):
    row = []
    for j in range(cols):
        # генерируем случайное число от 0 до 20
        num = random.randint(0, 20)
        row.append(num)
    matrix.append(row)

# выводим исходную матрицу
print("Исходная матрица:")
for row in matrix:
    print(row)

# заменяем элементы, больше 10, на 0
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] > 10:
            matrix[i][j] = 0

# выводим переделанную матрицу
print("Переделанная матрица:")
for row in matrix:
    print(row)