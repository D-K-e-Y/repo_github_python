# имя, фамилия, год рождения, город проживания, email, телефон
trt = []
char = {'Имя': '', 'Фамилия': '', 'Год рождения': '', 'Город проживания': '', 'email': '', 'Телефон': ''}
analytics = {'': []}
num = 0
user_data = None
control = None
while True:
    control = input("Для выхода введите 'Q'\n Для аналитики введите 'A'\n Для ввода данных нажмите 'Enter'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'Данные пользователя:')
        for key, value in char.items():
            far = " ".join((str(v)) for k,v in char.items())
            print(far)
            break
    for n in char.keys():
        user_data = input(f'Введите данные "{n}" :')
        char[n] = user_data
    trt.append((num, char))
#test