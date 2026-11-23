lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

total = 0

for char in lst1:
    if (type(char) == int or (type(char) == str and char.isdigit())) and int(char) % 2 == 0:
        total += int(char)

print(total)

# type(char) == int - проверяем числа
# type(char) == str and char.isdigit - проверяем строки, где есть цифра
# int(char) % 2 == 0 - деление без остачи, проверка на четное число