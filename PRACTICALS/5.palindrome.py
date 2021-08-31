print('A palindrome is a word or sequence that reads the same backwards as forwards')

def loop():
    choice = input('Want to continue (y/n) \n=>')
    if choice == 'y':
        program()
    else:
        print('Program ended!!')

def program():
    word = input('Enter a word to chek whether it is palindrome: ')
    if word[: :-1] == word:
        print('Palindrome')
    else:
        print('Not a palindrome')
    loop()


program()