adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ") # змінюємо переноси рядків
print(adwentures_of_tom_sawer)
# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ") # замюємо .. на побіл
print(adwentures_of_tom_sawer)
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split()) # видяляємо зайві пробіли
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
letter_to_find = 'h'
index_letter = adwentures_of_tom_sawer.find(letter_to_find)
print(f'{adwentures_of_tom_sawer.count(letter_to_find)} раз зустрічається літера {letter_to_find} у тексті')
#print(adwentures_of_tom_sawer.count('h')) перевірка на count

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
count = 0
for words in adwentures_of_tom_sawer.split(): # разділяє тест на слова
    words = words.lstrip('"') # прибирає кавичку на початку слова
    if words[0].isupper(): #  [0] тільки першу букву перевіряє
        count += 1
print(f'{count} слів у тексті починається з Великої літери')

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
word_to_find = 'Tom'
index_word_start = adwentures_of_tom_sawer.find(word_to_find)
index_word_second = adwentures_of_tom_sawer.find(word_to_find, index_word_start + 1)
print(f'слово Tom зустрічається вдруге на {index_word_second} позиції')


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('.')
print(adwentures_of_tom_sawer_sentences)


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(f'Четверте речення в нижньому регістрі: {adwentures_of_tom_sawer_sentences[3].lower()}')

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for  sentence in adwentures_of_tom_sawer_sentences:
    if sentence.strip().startswith('By the time'):
      print(f'Є рядок, що починається з: {sentence}')

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-2].rstrip('.')
print(last_sentence)