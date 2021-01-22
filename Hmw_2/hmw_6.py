goods = []
char = {'Название': '', 'Цена': '', 'Количество': ''}
analytics = {'Название': [], 'Цена': [], 'Количество': []}
num = 0
user_feature = None
control = None
while True:
    control = input("Для выхода введите 'Q'\n Для аналитики введите 'A'\n Для ввода данных нажмите 'Enter'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'Current analytics:')
        for key, value in analytics.items():
            print(f'{key}: {value}')
    for n in char.keys():
        user_feature = input(f'Введите данные "{n}" :')
        char[n] = int(user_feature) if (n == 'Цена' or n == 'Количество') else user_feature
        analytics[n].append(char[n])
    goods.append((num, char))
#test#test#test