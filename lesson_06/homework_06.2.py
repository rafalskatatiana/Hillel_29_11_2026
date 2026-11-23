some_word = input('Enter a word containing the letter h: ')
while 'h' not in some_word.lower():
    print('Wrong word, please try again')
    some_word = input('Enter a word containing the letter h: ')

print('Correct word:', some_word)







  #№2
# while True:
#     some_word = input('Enter a word containing the letter h:')
#     if 'h' not in some_word.lower():
#             print('Wrong word, please try again')
#             continue
#     print('Correct word:', some_word)
#     break