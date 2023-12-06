"""
Задача 23 : Дано натуральное число n.
Определите, является ли оно членом
последовательности Фибоначчи.
"""

# получаем число для проверки
num = int(input('Введите натуральное число : '))
n1, n2 = 0, 1
sm_ch = 0

text_yes = f'Да, число {num} является членом последовательности Фибоначчи'
text_no = f'Нет, число {num} не является членом последовательности Фибоначчи'

# генерируем поселдовательность поэлементно
while num >= sm_ch:
    sm_ch = n1 + n2
    if sm_ch == num:
        print(text_yes)
        break
    n1 = n2
    n2 = sm_ch
else:
    print(text_no)
