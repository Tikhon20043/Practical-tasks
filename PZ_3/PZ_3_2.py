#Даны четыре целых числа, одно из которых отлично от трех других, равных между
#собой. Определить порядковый номер числа, отличного от остальных.

a, b, c, d = input("Введите первое число: "), input("Введите второе число: "), input("Введите третье число: "), input("Введите четвёртое число: ")

while type(a) != int: # обработка исключений
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите первое число: ")
while type(b) != int: # обработка исключений
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите второе число: ")
while type(c) != int: # обработка исключений
    try:
        c = int(c)
    except ValueError:
        print("Неправильно ввели!")
        c = input("Введите третье число: ")
while type(d) != int: # обработка исключений
    try:
        d = int(d)
    except ValueError:
        print("Неправильно ввели!")
        d = input("Введите третье число: ")



if a == b and b == c:
    print("Порядковый номер числа отличного от остальных: 4")
elif a == b and b == d:
    print("Порядковый номер числа отличного от остальных: 3")
elif a == c and c == d:
    print("Порядковый номер числа отличного от остальных: 2")
else:
    print("Порядковый номер числа отличного от остальных: 1")
