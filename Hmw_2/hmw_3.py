# list:
seasons_list = ['winter', 'spring', 'summer', 'autumn']
number_month = int(input('Введите номер месяца: '))
if number_month == 1 or number_month == 2 or number_month == 12:
    print(seasons_list[0])
elif number_month == 3 or number_month == 4 or number_month == 5:
    print(seasons_list[1])
elif number_month == 6 or number_month == 7 or number_month == 8:
    print(seasons_list[2])
elif number_month == 9 or number_month == 10 or number_month == 11:
    print(seasons_list[3])

# dict:
seasons_dict = {'season_1': 'winter', 'season_2': 'spring', 'season_3': 'summer', 'season_4': 'autumn'}
number_month = int(input('Введите номер месяца: '))
if number_month == 1 or number_month == 2 or number_month == 12:
    print(seasons_dict.get('season_1'))
elif number_month == 3 or number_month == 4 or number_month == 5:
    print(seasons_dict.get('season_2'))
elif number_month == 6 or number_month == 7 or number_month == 8:
    print(seasons_dict.get('season_3'))
elif number_month == 9 or number_month == 10 or number_month == 11:
    print(seasons_dict.get('season_4'))
