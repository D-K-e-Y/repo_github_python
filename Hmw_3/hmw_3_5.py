def my_sum():
    sum = 0
    while True:
        user_number = input('Для выхода введите Q.\nВведите строку чисел, разделенных пробелом: ').split()
        nums = 0
        for el in range(len(user_number)):
            if user_number[el] == 'Q':
                break
            else:
                nums = nums + int(user_number[el])
        sum = sum + nums
        print(f'Сумма чисел: {sum}')
my_sum()
#test