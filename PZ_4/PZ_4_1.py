#Дано целое число N (>0). Найти значение выражения 1.1 - 1.2 + 1.3 - ...
#(N слагаемых,знаки чередуются).
N = int(input("Введите целое число N: "))  # Запросить у пользователя целое число N

while type(N) != int:  # Обработка исключений, если пользователь ввел не целое число
    try:
        N = int(N)
    except ValueError:
        print("Неправильно ввели!")
        N = input("Введите целое число N: ")
result = 0
i = 1
while i <= N:
    term = (-1) ** (i + 1) * (1 + i / 10)  # Вычислить слагаемое с учетом знака
    result += term  # Добавить слагаемое к результату
    i += 1

print("Значение выражения:", result)  # Вывести значение выражения на экран
