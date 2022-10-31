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
# import re


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
#
# a = [input("-> ") for i in range(int(input("n = ")))]
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")
#
#
# n = 9
# for a in range(n):
#     for i in range(a):
#         print("*", end=" ")
#     print(" ")
#
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
# m = 0
# n = [[r.randint(-20, 10) for x in range(3)] for b in range(4)]
#
# for row in n:
#     for x in row:
#         if x < 0:
#             m += 1
#         print(x, end="\t\t")
#     print()
# print("Количество отрицательных элементов: ", m)

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


# Домашнее задание №18
#
# import re
#
# s = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
# print(re.findall("[a-яA-Я0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+", s))

# Домашнее задание №19

# def validate_password(password):
#     return re.findall(r'^[a-zA-Z\d@_-]{8,18}$', password)
#
#
# print(validate_password('my-p@ssw0rd'))

# s = "В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков."
# reg = r'\d{2}/\d{2}/\d{4}'
# print(re.findall(reg, s))


# Домашнее задание №20

# Рекурсия Вариант №1
# def count(lst):
#     if len(lst) == 1:
#         if lst[0] < 1:
#             return 1
#         else:
#             return 0
#     else:
#         if lst[0] < 1:
#             return 1 + count(lst[1:])
#         else:
#             return count(lst[1:])
#
#
# print("n = :", count([-2, 3, 8, -11, -4, 6]))


# Рекурсия Вариант №2
# def count(lst):
#     return (1 if lst[0] < 0 else 0) + count(lst[1:]) if lst else 0
#
#
# print("n = :", count([-2, 3, 8, -11, -4, 6]))
#

# Домашнее задание №21

# Задача 1
# my_file = open("text.txt", "w")
# my_file.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
# my_file.close()
#
# my_file = open("text.txt", "r")
# read_file = my_file.readlines()
# print(read_file)
# read_file[1], read_file[2] = read_file[2], read_file[1]
# print(read_file)
# my_file.close()
#
# my_file = open("text.txt", "w")
# my_file.writelines(read_file)
# my_file.close()

# Задача 2

# my_file = open("text1.txt", "w")
# my_file.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
# my_file.close()
#
# my_file = open("text1.txt", "r")
# read_file = my_file.readlines()
# print(read_file)
# read_file1 = read_file[::-1]
# print(read_file1)
# my_file.close()
#
# my_file = open("text1.txt", "w")
# my_file.writelines(read_file1)
# my_file.close()

# Задача 3

# my_file = open("firstfile.txt", "w")
# my_file.write("Привет, мир!")
# my_file.close()
# my_file = open("secondfile.txt", "w")
# my_file.write("Hello world!")
# my_file.close()
# my_file = open("firstfile.txt", "w")
# my_file.write(" ")
# my_file.close()

# first_filename = "firstfile.txt"
# second_filename = "secondfile.txt"
# third_filename = "thirdfile.txt"
#
# with open(first_filename, 'r') as file:
#     first_file_content = file.read()
#
# with open(second_filename, 'r') as file:
#     second_file_content = file.read()
#
# with open(third_filename, 'w') as file:
#     file.write(first_file_content + second_file_content)

# Домашнее задание №22

# class Book:
#     title_book = "title_book"
#     year_production = "year_production"
#     publisher = "publisher"
#     genre = "genre"
#     author = "author"
#     price = "price"
#
#     def print_info(self):
#         print("=" * 40)
#         print(f"Название книги: {self.title_book}\nГод выпуска: {self.year_production}\n"
#               f"Издание: {self.publisher}\nЖанр: {self.genre}\nАвтор: {self.author}\n"
#               f"Цена: {self.price}")
#         print("=" * 40)
#
#     def input_info(self, title_book, year_production, publisher, genre, author, price):
#         self.title_book = title_book
#         self.year_production = year_production
#         self.publisher = publisher
#         self.genre = genre
#         self.author = author
#         self.price = price
#
#     def set_title_book(self, title_book):
#         self.title_book = title_book
#
#     def get_title_book(self):
#         return self.title_book
#
#     def set_year_production(self, year_production):
#         self.year_production = year_production
#
#     def get_year_production(self):
#         return self.year_production
#
#     def set_publisher(self, publisher):
#         self.publisher = publisher
#
#     def get_publisher(self):
#         return self.publisher
#
#     def set_genre(self, genre):
#         self.genre = genre
#
#     def get_genre(self):
#         return self.genre
#
#     def set_author(self, author):
#         self.author = author
#
#     def get_author(self):
#         return self.author
#
#     def set_price(self, price):
#         self.price = price
#
#     def get_price(self):
#         return self.price
#
#
# b1 = Book()
# b1.input_info("Начинаем программировать на>>> Python", "2022", "БВХ-Петербург", "Обучающая литература", "Тони Гэддис",
#               "1500 руб")
# b1.print_info()
# b1.set_title_book("Python3 Самое необходимое")
# print(b1.get_title_book())
# b1.set_year_production("2019")
# print(b1.get_year_production())
# b1.set_publisher("БВХ Санкт-Петербург")
# print(b1.get_publisher())
# b1.set_genre("Программирование")
# print(b1.get_genre())
# b1.set_author("Н.А. Прохоренок, В.А. Дронов")
# print(b1.get_author())
# b1.set_price("1000 руб")
# print(b1.get_price())
# print("=" * 40)


# Домашнее задание №23
# import math
#
#
# class Rectangle:
#
#     def __init__(self, length=0, width=0):
#         self.__length = length
#         self.__width = width
#
#     def set_length(self, length):
#         if isinstance(length, int) or isinstance(length, float):
#             self.__length = length
#         else:
#             print("Длина должна быть числом")
#
#     def get_length(self):
#         return self.__length
#
#     def set_width(self, width):
#         if isinstance(width, int) or isinstance(width, float):
#             self.__width = width
#         else:
#             print("Ширина должна быть числом")
#
#     def get_width(self):
#         return self.__width
#
#     def getSquare(self):
#         return self.__length * self.__width
#
#     def getPerimeter(self):
#         return 2 * (self.__length + self.__width)
#
#     def getHypotenuse(self):
#         return math.sqrt(self.__length * self.__length + self.__width * self.__width)
#
#     def print_rectangle(self):
#         for i in range(self.__length):
#             for j in range(self.__width):
#                 print("*", end="")
#             print()
#
#
# r1 = Rectangle()
# r1.set_length(3)
# r1.set_width(9)
# print(f"Длина прямоугольника: {r1.get_length()}")
# print(f"Ширина прямоугольника: {r1.get_width()}")
# print(f"Площадь прямоугольника: {r1.getSquare()}")
# print(f"Периметр прямоугольника: {r1.getPerimeter()}")
# print(f"Гипотенуза прямоугольника: {r1.getHypotenuse():.2f}")
# print(r1.print_rectangle())

# Домашнее задание №24

# class Conveyor:
#
#     def __init__(self, wt):
#         self.__wt = wt
#
#     @property
#     def wt(self):
#         return self.__wt
#
#     @wt.setter
#     def wt(self, wt):
#         if isinstance(wt, int) or isinstance(wt, float):
#             self.__wt = wt
#         else:
#             print("Вес должен быть целочисленным или вещественным числом")
#
#
# c1 = Conveyor(12)
# print(f"12 кг => {c1.wt * 2.20462262185:.2f} фунтов")
#
# c2 = Conveyor(41)
# print(f"41 кг => {c2.wt * 2.20462262185:.3f} фунтов")


# Домашнее задание №25

# Вариант №1
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f'Счет #{self.__num} принадлежит {self.__surname} был открыт.')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.__num} принадлежащий {self.__surname} был закрыт.')
#         print()
#
#     def get_num(self):
#         return self.__num
#
#     def set_num(self, num):
#         self.__num = num
#
#     def get_surname(self):
#         return self.__surname
#
#     def set_surname(self, surname):
#         self.__surname = surname
#
#     def get_percent(self):
#         return self.__percent
#
#     def set_percent(self, percent):
#         self.__percent = percent
#
#     def get_value(self):
#         return self.__value
#
#     def set_value(self, value):
#         self.__value = value
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def edit_owner(self, surname):
#         self.__surname = surname
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}.')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}.')
#
#     def print_balance(self):
#         print(f'Текущий баланс {self.__value} {Account.suffix}')
#
#     def print_info(self):
#         print(f'Информация о счете:')
#         print('-' * 20)
#         print(f'#{self.__num}')
#         print(f'Владелец: {self.__surname}')
#         self.print_balance()
#         print(f'Проценты: {self.__percent:.0%}')
#         print('-' * 20)
#
#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#         print('Проценты были успешно начислены')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f'К сожалению у вас нет {val} {Account.suffix}')
#         else:
#             self.__value -= val
#             print(f'{val} {Account.suffix} было успешно снято!')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
#
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
#
# acc.edit_owner('Дюма')
# acc.print_info()
# print()
#
# acc.add_percents()
# print()
#
# acc.withdraw_money(3000)
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()


# Вариант №2
#
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f'Счет #{self.__num} принадлежит {self.__surname} был открыт.')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.__num} принадлежащий {self.__surname} был закрыт.')
#         print()
#
#     @property
#     def num(self):
#         return self.__num
#
#     @num.setter
#     def num(self, num):
#         self.__num = num
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, surname):
#         self.__surname = surname
#
#     @property
#     def percent(self):
#         return self.__percent
#
#     @percent.setter
#     def percent(self, percent):
#         self.__percent = percent
#
#     @property
#     def value(self):
#         return self.__value
#
#     @value.setter
#     def value(self, value):
#         self.__value = value
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def edit_owner(self, surname):
#         self.__surname = surname
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}.')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}.')
#
#     def print_balance(self):
#         print(f'Текущий баланс {self.__value} {Account.suffix}')
#
#     def print_info(self):
#         print(f'Информация о счете:')
#         print('-' * 20)
#         print(f'#{self.__num}')
#         print(f'Владелец: {self.__surname}')
#         self.print_balance()
#         print(f'Проценты: {self.__percent:.0%}')
#         print('-' * 20)
#
#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#         print('Проценты были успешно начислены')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f'К сожалению у вас нет {val} {Account.suffix}')
#         else:
#             self.__value -= val
#             print(f'{val} {Account.suffix} было успешно снято!')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
#
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
#
# acc.edit_owner('Дюма')
# acc.print_info()
# print()
#
# acc.add_percents()
# print()
#
# acc.withdraw_money(3000)
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)


# Домашнее задание №26
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#     def is_digit(self):
#         if not isinstance(self.__x, (int, float)) or not isinstance(self.__y, (int, float)):
#             print("Координаты должны быть числами")
#             return False
#         return True
#
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print("Координаты должны быть целочисленными")
#             return False
#         return True
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#
#
# class Line(Prop):
#
#     def draw_line(self) -> None:
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#     def set_coords(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#
#
# class Rect(Prop):
#
#     def draw_rect(self) -> None:
#         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(10.2, 20), Point(100, 200))
# line.draw_line()
#
# rect = Rect(Point(7, 9), Point(12, 15))
# rect.draw_rect()
# rect.set_coords(Point(30.5, 40.2), Point(50, 60))
# rect.draw_rect()

# Домашнее задание №27
# class Liquid:
#     def __init__(self, name, density):
#         self.name = name
#         self.density = density
#
#     def edit_density(self, val):
#         self.density = val
#
#     def calc_v(self, m):
#         v = m / self.density
#         print(f'Объем {m} кг {self.name} равен {v} m^3')
#
#     def calc_m(self, v):
#         m = v * self.density
#         print(f'Вес {v} m^3 of {self.name} составляет {m} кг.')
#
#     def print_info(self):
#         print(f"Жидкость '{self.name}' (плотность = {self.density} kg/m^3).")
#
#
# class Alcohol(Liquid):
#     def __init__(self, name, density, strength):
#         super().__init__(name, density)
#         self.strength = strength
#
#     def edit_strength(self, val):
#         self.strength = val
#
#
# a = Alcohol('Wine', 1064.2, 14)
# a.print_info()
#
# a.edit_density(1000)
# a.print_info()
#
# a.calc_v(300)
# a.calc_m(0.5)
#
# print(a.strength)
# a.edit_strength(20)
# print(a.strength)


# Домашнее задание №28

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.notebook = self.Notebook()
#
#     class Notebook:
#         def make(self):
#             return "HP"
#
#         def model(self):
#             return "i7"
#
#         def ram(self):
#             return "16"
#
#
# st1 = Student('Roman')
# my_notebook = st1.notebook
# print(f'{st1.name} => {my_notebook.make()}, {my_notebook.model()}, {my_notebook.ram()}')
# st2 = Student('Vladimir')
# my_notebook = st2.notebook
# print(f'{st2.name} => {my_notebook.make()}, {my_notebook.model()}, {my_notebook.ram()}')

# Домашнее задание №29
# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#
#         self.sec = sec % self.__DAY
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec + other.sec)
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec - other.sec)
#
#     def __mul__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError()
#         return Clock(self.sec * other.sec)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError()
#         return Clock(self.sec // other.sec)
#
#     def __mod__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError()
#         return Clock(self.sec % other.sec)
#
#     def __eq__(self, other):
#         return self.sec == other.sec
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __gt__(self, other):
#         return self.sec > other.sec
#
#     def get_format_time(self):
#         s = self.sec % 60  # секунды
#         m = (self.sec // 60) % 60  # минуты
#         h = (self.sec // 3600) % 24  # часы
#         return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if item == "hour":
#             return (self.sec // 3600) % 24
#         elif item == "min":
#             return (self.sec // 60) % 60
#         elif item == "sec":
#             return self.sec % 60
#
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом ")
#         s = self.sec % 60  # секунды
#         m = (self.sec // 60) % 60  # минуты
#         h = (self.sec // 3600) % 24  # часы
#         if key == "hour":
#             self.sec = s + 60 * m + value * 3600
#         elif key == "min":
#             self.sec = s + 60 * value + h * 3600
#         elif key == "sec":
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
# print(c1["hour"], c1["min"], c1["sec"])
# c1["hour"] = 10
# print(c1["hour"], c1["min"], c1["sec"])

# Домашнее задание №30
# import math
# from abc import ABC, abstractmethod
#
#
# class Share(ABC):
#     def __init__(self, color):
#         self.color = color
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#     @abstractmethod
#     def square(self):
#         pass
#
#     @abstractmethod
#     def draw(self):
#         pass
#
#
# class Square(Share):
#     def __init__(self, w, color):
#         self.w = w
#         super().__init__(color)
#
#     def perimeter(self):
#         perimeter = self.w * 4
#         return perimeter
#
#     def square(self):
#         return self.w * self.w
#
#     def draw(self):
#         return ('*' * self.w + '\n') * self.w
#
#     def info(self):
#         print(f"===Квадрат===\nСторона: {self.w}\nЦвет: {self.color}\nПлощадь: {self.square()}\nПериметр:"
#               f" {self.perimeter()}\n{self.draw()} ")
#
#
# class Rectangle(Share):
#     def __init__(self, w, h, color):
#         self.w = w
#         self.h = h
#         super().__init__(color)
#
#     def perimeter(self):
#         perimeter = self.w * 2 + self.h * 2
#         return perimeter
#
#     def square(self):
#         return self.w * self.h
#
#     def draw(self):
#         return ('*' * self.h + '\n') * self.w
#
#     def info(self):
#         print(
#             f"===Квадрат===\nДлина: {self.w}\nШирина: {self.h}\nЦвет: {self.color}\nПлощадь: {self.square()}\nПериметр:"
#             f" {self.perimeter()}\n{self.draw()} ")
#
#
# class Triangle(Share):
#     def __init__(self, w, h, l, color):
#         self.w = w
#         self.h = h
#         self.l = l
#         super().__init__(color)
#
#     def perimeter(self):
#         return (self.w + self.h + self.l) / 2
#
#     def square(self):
#         return self.w / 4 * math.sqrt(4 * self.h ** 2 - self.w ** 2)
#
#     def draw(self):
#         rows = []
#         for n in range(self.h):
#             rows.append(" " * n + "*" * (self.w - 2 * n) + " " * n)
#         print("\n".join(reversed(rows)))
#
#     def info(self):
#         print(
#             f"===Треугольник===\nСторона 1: {self.w}\nСторона 2: {self.h}\nСторона 3: {self.l}\nЦвет: {self.color}\nПлощадь: {self.square(): .2f}\nПериметр:"
#             f" {self.perimeter()}")
#
#
# s = Square(3, 'red')
# s.info()
# r = Rectangle(3, 7, 'green')
# r.info()
# t = Triangle(11, 6, 6, 'yellow')
# t.info()
#
# a = (s, r, t)
# for i in a:
#     i.draw()

# Домашнее задание №31


# class OldOrder:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if value <= 0:
#             raise ValueError(f"{self.__name} число должно быть положительным")
#         instance.__dict__[self.__name] = value
#
#
# class Order:
#     price = OldOrder()
#     amount = OldOrder()
#
#     def __init__(self, name, price, amount):
#         self.name = name
#         self.price = price
#         self.amount = amount
#
#     def sum(self):
#         return self.price * self.amount
#
#
# o = Order('apple', 5, 10)
# print(f'Тест:\nOrder ({o.name}, {o.price}, {o.amount})')
# print(o.sum())

# Домашнее задание №32
class Number:
    @classmethod
    def verify(cls, coord):
        if not isinstance(coord, int) or coord <= 0:
            raise TypeError(f"Координата {coord} должна быть положительным целым числом")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify(value)
        setattr(instance, self.name, value)


class Triangle:
    a = Number()
    b = Number()
    c = Number()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def existence(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return "существует"
        else:
            return "не существует"

    def info(self):
        print(f"Треугольник со сторонами ({self.a}, {self.b}, {self.c}) {self.existence()}")


t1 = Triangle(2, 5, 6)
t2 = Triangle(5, 2, 8)
t3 = Triangle(7, 3, 6)

tr = [t1, t2, t3]
for i in tr:
    i.info()

