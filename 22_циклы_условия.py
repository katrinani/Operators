"""
Задача 22 : Даны n вещественных чисел.
Определите максимальное и минимальное из них.
"""

#
quantity = int(input('Введите количество чисел : '))
mx_ch = -1000000
mn_ch = 1000000

#
for num in range(quantity):
    ch = float(input(f'Введите {num + 1} число : '))
    if ch > mx_ch:
        mx_ch = ch
        if ch < mn_ch:
            mn_ch = ch
    else:
        continue

print('Минимальное число равно', round(mn_ch, 2))
print('Максимальное число равно', round(mx_ch, 2))
