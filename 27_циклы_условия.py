"""
Задача 27 :
Выведите на экран (в строку) n первых простых чисел.
"""

#  получаем количество чисел
n = int(input('Введите количетво чисел : '))
ch = 1
count = 0
flag = True

print(f'Первые {n} простых чисел :')
# проверяем числа на делимость
while count <= n:
    for i in range(2, ch):  # делители не равные 1 и самомому числу
        if ch % i == 0:
            flag = False
    if flag == True:
        print(ch, end=' ')
        count += 1
    ch += 1
    flag = True
