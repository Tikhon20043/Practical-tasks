#Дан список размера N и целое число K (1 < K < N). Осуществить сдвиг элементов
#списка вправо на K позиций (при этом A1 перейдет в AK+1, A2 — в AK+2, ..AN-K — в
#AN, а исходное значение K последних элементов будет потеряно). Первые K
#элементов полученного списка положить равными 0.

A = [1, 2, 3, 4, 5]  # Пример списка A
N = len(A)  # Размер списка A
K = 3  # Число K

B = [0] * K + A[:N-K]  # Первые K элементов списка B равны 0, остальные элементы взяты из списка A с учетом сдвига
print(B)  # Вывод списка B