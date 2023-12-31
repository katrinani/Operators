"""
Задача 14 : Начав тренировки, лыжник в первый
день пробежал s км. (s>0, вещественное число).
Каждый следующий день он увеличивал пробег на
p % (0<p≤100, вещественное число) от пробега предыдущего дня.
Определите:
• пробег лыжника за второй, третий, …, десятый день тренировок;
• какой суммарный путь он пробежал за первые 10 дней тренировок.
"""

# получаем значения переменных
s = float(input('Введите растояние для 1 дня тренировки : '))
p = float(input('Введите коэфицент увелеичения растояния : '))

all_values_s = [s]
sum_s = s

# считаем растояние с 2 по 10 день, добавляем в список и считаем сумму
for i in range(2, 11):
    s_day = s * p ** (i - 1)
    all_values_s.append(round(s_day, 1))
    sum_s += s_day

# выводим значения
print(f'Суммарный путь за 10 дней равен {round(sum_s)}, а конкретней :')
for i in range(10):
    print(f'В {i + 1} день - {all_values_s[i]} км.')

