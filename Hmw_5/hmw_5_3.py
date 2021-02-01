with open('hmw_5_3.txt', 'r') as f:
    min = []
    str = []
    my_list = f.read().split('\n')
    f = sorted(f)
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           min.append(i[0])
        str.append(i[1])
    val = sum(map(int, str)) / len(str)
print(f'Оклад меньше 20000: {min} \nСредняя величина дохода сотрудников: {val}')
#test