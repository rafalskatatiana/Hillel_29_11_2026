some_word = input('Enter a word containing the letter h:')
for char in some_word:
    if 'h' in some_word.lower():
        print('Correct word')
        break
else:
    print('Wrong word, please try again')
