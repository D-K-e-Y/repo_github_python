# x/y
def my_funk(x, y):
    while True:
        if y == 0:
            print('Делить на 0 нельзя!')
            break
        else:
            x = x / y
            return x
print(f'Результат: ', my_funk(x = (int(input("Введите x: "))), y = (int(input("Введите y: ")))))
#test