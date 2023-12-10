"""
Задача 31 : Дано предложение.
Выведите его на экран, удалив из него все слова,
содержащие произвольную букву (вводится с клавиатуры).
"""

# получаем предложение и букву
words = input('Введите предложение : ').split()
off_letter = input('Введите букву : ')
new_words = []

# проверяем все слова на наличие буквы
for word in words:
    flag = all(letter != off_letter for letter in word)
    if flag == True:
        new_words.append(word)

print(*new_words)
