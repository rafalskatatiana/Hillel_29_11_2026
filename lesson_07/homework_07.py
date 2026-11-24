# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""

def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 25:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(f"{number} x {multiplier} = {result}")

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def summ_number(first_number, second_number):
    return first_number + second_number
print(summ_number(first_number=10, second_number=39))


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
numbers = [20, 12, 19, 25, 14]
def average_numbers(numbers):
    if len(numbers) >0:
        return sum(numbers) / len(numbers)
    else:
        return 0
print(average_numbers(numbers))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
list = ['a', 'b', 'c', 'd', 'e']
def lst(list):
    return list
list.reverse()
print(lst(list))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
list = ['home','gitcommit','consequences','cat']
def words_of_list(words):
    longest_word = max(words, key=len)
    return longest_word
print(words_of_list(list))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
def calculate_tress(apple_tree):
    '''
    Обчіслює загальну кількість дерев у саду
    :param apple_tree: кількість яблунь
    :return: загальна кількість яблунь,груш та слив
    '''

    pear_tree = apple_tree + 5
    plum_tree = apple_tree - 2
    total_trees = apple_tree + pear_tree + plum_tree
    return total_trees
print(calculate_tress(apple_tree=4))

def calculate_pages(total_image, image_per_page):
    '''
    Обчіслює кількість сторінок, необхідних для розміщення фото
    :param total_image: загальна кількість фото
    :param image_per_page: кількість фотографій на одній сторінці
    :return: необхідна кількість сторінок
    '''
    pages = total_image // image_per_page
    return pages
print(calculate_pages(total_image=232,image_per_page=8))


def get_string_value(input_list):
    '''
    Повертає новий список, що містить лише рядки
    :param input_list: список єлементів різних типів
    :return: новий список, що містить тільки рядки
    '''
    get_string_value = [x for x in input_list if type(x) == str]
    return get_string_value
lst= ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
print(get_string_value(lst))


def calculate_computer_cost(monthly_payment, month_count):
    '''
    Обчіслює загальну вартість комп'ютера за щомісячними платежами
    :param monthly_payment: сума щомісячного платежу
    :param month_count: кількість місяців оплати
    :return: загальна вартість комп'ютера в грн
    '''
    total_cost = monthly_payment * month_count
    return total_cost
print(calculate_computer_cost(monthly_payment=1179, month_count=18))

