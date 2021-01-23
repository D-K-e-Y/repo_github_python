def int_func():
    while True:
        words = input('Введите текст: ')
        if words == 'Q':
                break
        else:
            print(words.title())
int_func()
#test