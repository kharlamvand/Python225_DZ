# Домашнее задание №2
# n = int(input("Введите число от 1 до 99: "))
# if 1 <= n <= 99:
#     if 11 <= n <= 14:
#         print(n, "копеек")
#     else:
#         x = n % 10
#         if x == 1:
#             print(n, "копейка")
#         if 2 <= x <= 4:
#             print(n, "копейки")
#         if 5 <= x <= 9 or x == 0:
#             print(n, "копеек")
# else:
#     print("Ошибка")

# Домашнее задание №3
# n = input('\n1 - "r" - Применяет унарный минус '
#           '\n2 - "+" - Сложение\n3 - "-" - Вычитание\n4 - "/" - Деление с остатком\n5 - "*" - Умножение'
#           '\n6 - "%" - Деление по модулю (остаток от деления)\n7 - "<" - Минимальное из двух чисел'
#           '\n8 - ">" - Максимальное из двух чисел\nВведите цифру: ')
# if n not in ('1', '2', '3', '4', '5', '6', '7', '8'):
#     print('Вы ввели неверный знак математической операции')
# if n == '1':
#     try:
#         num1 = int(input('Введите первое число: '))
#         num1 = - num1
#         print('Результат: ', num1 )
#     except ValueError:
#         print('Вы ввели не целое число')
# if n == '2':
#     try:
#         num3 = int(input('Введите первое число: '))
#         num4 = int(input('Введите второе число: '))
#         print('Результат: ', num3 + num4)
#     except ValueError:
#         print('Вы ввели не целое число')
# if n == '3':
#     try:
#         num5 = int(input('Введите первое число: '))
#         num6 = int(input('Введите второе число: '))
#         print('Результат: ', num5 - num6)
#     except ValueError:
#         print('Вы ввели не целое число')
# if n == '4':
#     try:
#         num7 = int(input('Введите первое число: '))
#         num8 = int(input('Введите второе число: '))
#         print('Результат: ', num7 / num8)
#     except ValueError:
#         print('Вы ввели не целое число')
#     except ZeroDivisionError:
#         print('На 0 делить нельзя')
# if n == '5':
#     try:
#         num9 = int(input('Введите первое число: '))
#         num10 = int(input('Введите второе число: '))
#         print('Результат: ', num9 * num10)
#     except ValueError:
#         print('Вы ввели не целое число')
# if n == '6':
#     try:
#         num11 = int(input('Введите первое число: '))
#         num12 = int(input('Введите второе число: '))
#         print('Результат: ', num11 % num12)
#     except ValueError:
#         print('Вы ввели не целое число')
#     except ZeroDivisionError:
#         print('На 0 делить нельзя')
# if n == '7':
#     try:
#         num13 = int(input('Введите первое число: '))
#         num14 = int(input('Введите второе число: '))
#         if num13 < num14:
#             print('Результат: ', num13)
#         else:
#             print('Результат: ', num14)
#     except ValueError:
#         print('Вы ввели не целое число')
# if n == '8':
#     try:
#         num15 = int(input('Введите первое число: '))
#         num16 = int(input('Введите второе число: '))
#         if num15 > num16:
#             print('Результат: ', num15)
#         else:
#             print('Результат: ', num16)
#     except ValueError:
#         print('Вы ввели не целое число')

# Домашнее задание №4
# n = 0  # число попыток угадать
# j = 47  # Заданное число
# while True:
#     g = int(input("Введите число от 0 до 100: "))
#     n += 1
#     if g == j:
#         print("Вы угадали загаданное число с ", n, "раза")
#         break
#     elif g == 0:
#         print('GAME OVER !!!')
#         break
#     elif g < j:
#         print("Загаданное число больше")
#     elif g > j:
#         print("Загаданное число меньше")

# Домашнее задание №5
# a = [input("-> ") for i in range(int(input("n = ")))]
# for i in range(0, len(a), 2):
#     print(a[i], end=" ")

# a = [input("-> ") for i in range(int(input("n = ")))]
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")


# n = 9
# for a in range(n):
#     for i in range(a):
#         print("*", end=" ")
#     print(" ")

# n = 9
# for a in range(n, 0, -1):
#     for i in range(1, a, + 1):
#         print("*", end=" ")
#     print(" ")

# Домашнее задание №6
# a = [1, 2, 3]
# b = [11, 12, 13, 7, 8]
# c = []
# print("a =", a)
# print("b =", b)
#
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# print("c =", c)


# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# for i in range(len(a)):
#     for j in range(len(a)):
#         if i != j and a[i] == a[j]:
#             break
#     else:
#         print(a[i], end=' ')

# Домашнее задание №6.1
# import random as r
# # m = 0
# # n = [[r.randint(-20, 10) for x in range(3)] for b in range(4)]
# #
# # for row in n:
# #     for x in row:
# #         if x < 0:
# #             m += 1
# #         print(x, end="\t\t")
# #     print()
# # print("Количество отрицательных элементов: ", m)
#
# n = [[r.randint(0, 4) for x in range(3)] for b in range(4)]
# m = 1
# for row in n:
#     for x in row:
#         if x > 0:
#             m *= x
#         print(x, end="\t\t")
#     print()
# print("Произведение ненулевых элементов: ", m)

# Домашнее задание №7
# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))

# Домашнее задание №8
# from math import sqrt
# from math import pi
#
#
# def square():
#     print("Укажите длину сторон прямоугольника:")
#     a = float(input("Сторона a = "))
#     b = float(input("Сторона b = "))
#     c = a * b
#     print("Площадь прямоугольника равна : ", round(c, 2))
#
#
# def rectangle():
#     print("Укажите длину сторон трехугольника:")
#     a = float(input("Сторона  a = "))
#     b = float(input("Сторона  b = "))
#     c = float(input("Сторона  c = "))
#     p = (a + b + c) / 2
#     s = sqrt(p * (p - a) * (p - b) * (p - c))
#     print("Площадь трехугольника равна : ", round(s, 2))
#
#
# def circle():
#     r = float(input("Укажите радиус круга R = "))
#     print("Площадь круга равна : ", (round(pi * r ** 2, 2)))
#
#
# print("прямоугольник - 1, треугольник - 2, круг - 3")
# figure = input("Выберите фигуру: ")
#
# if figure == '1':
#     square()
#
# if figure == '2':
#     rectangle()
#
#
# if figure == '3':
#     circle()

# Домашнее задание №9
# tpl = ('ab', 'abcd', 'cde', 'adc', 'def')
# inp = input("s = : ")
# for i in tpl:
#     if i in inp:
#         print("YES")
#
# s = ('2', '5', '3', '5', '2', '3', '6', '5', '1')
# for i in s:
#     print(i, end="")
# print()
# print("Количество 2 =", s.count('2'))
# print("Количество 5 =", s.count('5'))
# print("Количество 3 =", s.count('3'))
# print("Количество 6 =", s.count('6'))
# print("Количество 1 =", s.count('1'))

# Домашнее задание №10

print(" С github все ок")