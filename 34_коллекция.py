"""
Задача 34
Вводится список из n годовых вкладов, предлагаемых банками, в формате:
Банк Сумма Процент
Далее определите (гарантируется, что искомый банк - один):
•самый доступный банк (с наименьшей первоначальной суммой);
•самый выгодный банк, принимая, что за год прибыль = сумма * процент / 100
"""

all_deposit = []
n = int(input('Введите количество вкладов в списке : '))

# создаем список словарей с информацией о банках
for i in range(n):
    deposit = input(f'Введите информацию (Банк Сумма Процент) о {i + 1} вкладе через пробел : ').split()
    all_deposit.append(
        {
            "name": deposit[0],
            "initial_sum": int(deposit[1]),
            "rate": float(deposit[2])
        }
    )

# сортируем банки по сумме и выводим название лучшего банка
sort_all_deposit = sorted(all_deposit, key=lambda bank: bank['initial_sum'])
print(
    f'Cамый доступный банк: {sort_all_deposit[0]["name"]} с первоначальной суммой {sort_all_deposit[0]["initial_sum"]}'
)

max_profit = 0
max_profit_bank = ''

# считаем у всех банков прибыли и находим самый прибыльный банк
for deposit in all_deposit:
    profit = round(deposit['initial_sum'] * deposit['rate'] / 100, 2)
    if max_profit < profit:
        max_profit = profit
        max_profit_bank = deposit['name']
print(f'Самый выгодный банк: {max_profit_bank} с прибылью {max_profit}')

# Банк1 4000 4.8
# Банк2 5000 2.0
