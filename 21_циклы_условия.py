"""
Задача 21 : Известно количество учеников в классе и их рост
(см.); рост мальчиков условно задан отрицательными
числами. Определите средний рост мальчиков и
средний рост девочек.
"""
sm_height_girl = 0
count_girl = 0
sm_height_boy = 0
count_boy = 0
# получаем количество учеников
quantity = int(input('Введите количество учеников : '))

# получаем рост каждого ученика и обрабатываем его
for num in range(quantity):
    height = int(input(f'Введите рост {num + 1} ученика : '))
    if height < 0:
        sm_height_boy += height
        count_boy += 1
    else:
        sm_height_girl += height
        count_girl += 1

# считаем среднее значение роста
sr_girl = sm_height_girl / count_girl
sr_boy = -sm_height_boy / count_boy

print(f'Средний рост девочек составляет {round(sr_boy, 1)} см.')
print(f'Средний рост мальчиков составляет {round(sr_girl, 1)} см.')
