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

# print(" С github все ок")

# print("Проверка работы ssh")

# Домашнее задание №11
# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# n = x.copy()
# n.update(y)
# print(n)

# Домашнее задание №12

# dict_one = {1: 10, 2: 20}
# dict_two = {3: 30, 4: 40}
# dict_three = {5: 50, 6: 60}
# merged_dict = dict_one | dict_two | dict_three
# print(merged_dict)


# dict_salary = {'emp1': {'name': 'Jhon', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000},
#                'emp3': {'name': 'Brad', 'salary': 6500}}
# print(dict_salary['emp3'])
# print(dict_salary['emp3']['salary'])
# salary = 8500
# dict_salary['emp3']['salary'] = salary
# for x in dict_salary:
#     print(x)
#     for y in dict_salary[x]:
#         print(y, ": ", dict_salary[x][y], sep="")

# students = {}
# n = int(input("Количество студентов: "))
# s = 0
# for i in range(n):
#     student_name = input(str(i + 1) + "-й студент: ")
#     point = int(input("Балл: "))
#     students[student_name] = point
#     s += point
# quantity = s / n
# print("Средний балл: %.0f. Студенты с баллом выше среднего:" % quantity)
# for i in students:
#     if students[i] > quantity:
#         print(i)

# Домашнее задание №13
# import math
#
# pi = math.pi
#
#
# def square(figure_type, **kwargs):
#     if figure_type == 'rhombus':
#         return kwargs['d1'] * kwargs['d2'] / 2
#     if figure_type == 'square':
#         return kwargs['a'] ** 2
#     if figure_type == 'trapezoid':
#         return 0.5 * (kwargs['a'] + kwargs['b']) * kwargs['h']
#     if figure_type == 'circle':
#         return pi * (kwargs['r'] ** 2)
#     else:
#         return 'Invalid data'
#
#
# print(square(figure_type='rhombus', d1=10, d2=8))
# print(square(figure_type='square', a=5))
# print(square(figure_type='trapezoid', a=12, b=3, h=6))
# print(square(figure_type='circle', r=18))
# print(square(figure_type='unknown', a=1, b=2, c=3))

# Домашнее задание №14

# print((lambda x, y, z: x * y * z)(2, 5, 5))


# students = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98},
# ]
#
# res1 = sorted(students, key=lambda item: item['name'])
# print(res1)
# res2 = sorted(students, key=lambda item: item['final'], reverse=True)
# print(res2)


# students = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98},
# ]
#
# man_evaluation = max(students, key=lambda item: item['final'])
# print(man_evaluation)
#
# min_evaluation = min(students, key=lambda item: item['final'])
# print(min_evaluation)

# nums = [3, 5, 7, 3, 9, 5, 7, 2]
#
# print(list(map(lambda t: t ** 2, nums)))
# print(list(map(lambda t: t ** 3, nums)))



# Домашнее задание №17

# my_str = "I am learning Python. hello, WORLD!"
# a = my_str[:my_str.find("h")]
# b = my_str[my_str.rfind("h") + 1:]
# print(a + b)


# my_str = "I am learning Python. hello, WORLD!"
# a = my_str[:my_str.find('h')]
# b = my_str[my_str.find('h'): my_str.rfind('h') + 1:]
# c = my_str[my_str.rfind('h') + 1:]
# my_str = a + b[::-1] + c
# print(my_str)


# print('Строка: ')
# s = input()
# print('Ее заменяемая подстрока: ')
# a = input()
# print('Новая подстрока: ')
# b = input()
#
# i = s.find(a)
# while i != -1:
#     x = len(a)
#     s = s[0:i] + b + s[i + x:]
#     i = s.find(a)
# print(s)

# my_str = "Ежевику для ежат Принесли два ежа. Ежевику еле-еле Ежата возле ели съели"
# my_str = my_str.split(" ")
# i = 0
# for x in my_str:
#     if x[0].lower() == "е":
#         i = i + 1
# print("Количество слов:", i)

print("Тест")
