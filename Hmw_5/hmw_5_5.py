with open('hmw_5_5.txt', 'w+') as f:
    data = input('Введите данные: ')
    f.writelines(data)
    my_numb = data.split()
    print(sum(map(int, my_numb)))