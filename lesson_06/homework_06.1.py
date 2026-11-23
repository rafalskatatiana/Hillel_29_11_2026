text = input('Введіть дані:')
uniq = [] # в этот список будем звписывать юник значения

for char in text:
    if char in uniq: # проверяем условие и есть ли char в списке
        continue # если  есть пропускаем и идем дальше
    else:
     uniq.append(char) # если символа нет добавляем в список
if len(uniq) > 10: # проверяем длину списка
    print(True)
else:
    print(False)


