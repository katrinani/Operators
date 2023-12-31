"""
Задача 29 : Дан список из n вещественных чисел, введенных с клавиатуры
(среди чисел есть по крайней мере одно положительное
и отрицательное число). Сформируйте из него 2 списка:
• положительных чисел, используя списковые включения;
• отрицательных чисел, не используя списковые включения.
• среднее арифметическое первого списка и среднее геометрическое второго списка.
"""

# получаем количество чисел и объявляем список всех чисел
n = int(input('Введите количество    чисел : '))
lst = []

# заполняем список значениями
for i in range(n):
    ch = float(input(f'Введите {i + 1} число : '))
    lst.append(ch)
print('Исходный список :', lst)

# формируем используя списковые включения
lst_plus = [lst[i] for i in range(n) if lst[i] >= 0]
print('Список положительных чисел :', lst_plus)

# формируем не используя списковые включения
lst_minus = []
for i in range(n):
    if lst[i] < 0:
        lst_minus.append(lst[i])
print('Список отрицательных чисел :', lst_minus)

# ищем среднее арифметическое отриц. чисел
sm_minus = 0
for i in lst_minus:
    sm_minus += int(i)
sr_arif = sm_minus / len(lst_plus)
print('Среднее арифметическое отриц. цисел :', round(sr_arif, 2))

# ищем среднее геометрическое полож. чисел
pr_plus = 1
for i in lst_plus:
    pr_plus *= int(i)
sr_geom = pr_plus ** (1 / 2)
print('Среднее геометрическое полож. чисел :', round(sr_geom, 2))
