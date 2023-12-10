"""
Задача 33 : Вводится список из n сотрудников в формате:
Фамилия Имя Отчество Пол Стаж
• определите самого «молодого» и самого «старого»
сотрудника, используя функцию sorted();
• сформируйте 2 отельных списка: мужчин и женщин и ответьте,
в каком из списков больше имен, начинающихся на
букву k (вводится с клавиатуры).
"""

n = int(input('Введите количество сотрудников : '))
all_employee = []

# создаем список всех сотрудников
for i in range(n):
    employee = input(f'Введите данные (Фамилия Имя Отчество Пол Стаж) {i + 1} сотрудника : ').split()
    all_employee.append(employee)

# сортируем список по стажу и выводим самого молодого и старого сотрудника
all_employee = sorted(all_employee, key=lambda employee: employee[4])
print(f'Самый "молодой" сострудник : {all_employee[0][1]} со стажем {all_employee[0][4]}')
print(f'Самый "cтарый" сострудник : {all_employee[n - 1][1]} со стажем {all_employee[n - 1][4]}')

k = input('Введите букву, с которой начинаются имена сотрудников : ')
count_woman = 0
woman_employee = []
count_man = 0
man_employee = []

# создаем списки мужчин и женщин и считаем имена, начинающиеся с нужной буквы
for employee in all_employee:
    if employee[3] == 'Ж':
        woman_employee.append(employee)
        if employee[1][0].lower() == k.lower():
            count_woman += 1
    else:
        man_employee.append(employee)
        if employee[1][0].lower() == k.lower():
            count_man += 1

# выводим списки жинщин и мужчин и вывод по количеству имен
print('Список женщин :', *woman_employee)
print('Список мужчин :', *man_employee)
if count_man > count_woman:
    print(f'Имен мужчин, начинающихся на букву {k}, больше чем имен женщин')
elif count_woman > count_man:
    print(f'Имен женщин, начинающихся на букву {k}, больше чем имен мужчин')
else:
    print(f'Количество имен мужчин и женщин, начинающихся на букву {k}, равно')

# Петрова Анна Алексеевна Ж 5
# Семенов Николай Михайлович М 2
# Сидорова Елена Семеновна Ж 3
