alice_in_wonderland = """Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."""
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
simbol = "'"
count=0
for char in alice_in_wonderland:
    if char == simbol:
        count += 1
print (f'Символ {simbol} у тексті зустрічається {count} рази');
print(alice_in_wonderland)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea = 436402
azove_sea = 37800
total_both_seass= black_sea + azove_sea
formatted_total = f"{total_both_seass:,}".replace(",", " ")
print(f'Чорне та Азовське моря разом мають площу {formatted_total} км2')


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_goods = 375291 # всьго на 3х складах товару
store_1_and_store_2 = 250449 # склад 1 + склад 2 разом
store_2_and_store_3 = 222950 # склад 2 + склад 3 разом
store_1 = total_goods - store_2_and_store_3
store_3 = total_goods - store_1_and_store_2
store_2 = store_1_and_store_2 - store_1
print(f'На першому складі: {store_1} товару\n'f'На другому складі: {store_2} товару\n'f'На третьому складі: {store_3} товару\n' )
#check_total = store_1 + store_3 + store_2
#print(check_total)


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
monthly_payment = 1179 # сума щомісячного платежу
credit_pay_month = 18 # термін виплати всього
total_cost = monthly_payment * credit_pay_month
formatted_cost = f"{total_cost:_}".replace("_", " ")
print(f'Вартість комп’ютера {formatted_cost} грн')


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
example_a = 8019 % 8
example_b = 9907 % 9
example_c = 2789 % 5
example_d = 7248 % 6
example_e = 7128 % 5
example_f = 19224 % 9
print(f'Остаток від ділення a: {example_a}\nОстаток від ділення b: {example_b}\nОстаток від ділення c: {example_c}\nОстаток від ділення d: {example_d}\nОстаток від ділення e: {example_e}\nОстаток від ділення f: {example_f}')

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_big_qty = 4
pizza_big_price = 274
pizza_midle_qty = 2
pizza_midle_price = 218
juse_qty = 4
juse_price = 35
cake_qty = 1
cake_price = 350
water_qty = 3
water_price = 21
total_cost = ((pizza_big_qty * pizza_big_price) + (pizza_midle_qty * pizza_midle_price) + (juse_qty *  juse_price)
              + (cake_qty * cake_price) + (water_qty + water_price))
formatted_cost = f"{total_cost:_}".replace("_", " ")
print(f"Загальна вартість замовлення: {formatted_cost} грн")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_image = 232
page_1 = 8
total_page = total_image // page_1
print(f"Ігорю знадобиться {total_page} сторінок")


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
total_distance_km = 1600
gas_per_100km = 9 # витрати бензину на 100км
tank_capacity_l = 48
gas_total_l = (total_distance_km * 9) // 100
how_many_times = gas_total_l // tank_capacity_l
print(f'Для подорожі знадобиться {gas_total_l} літрів бензину.')
print(f'Під час подорожі необхідно заїхати на заправку щонайменше {how_many_times} рази.')
