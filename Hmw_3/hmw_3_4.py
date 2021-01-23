# x^y
def my_funk(x, y):
    x = x**y
    return x
print(f'Результат: ', my_funk(x = (int(input("Введите x: "))), y = (int(input("Введите y: ")))))

### while
def my_funk(x, y):
    while y:
        x = 1/(x * x)
        return x
print(f'Результат: ', my_funk(x = (int(input("Введите x: "))), y = (int(input("Введите y: ")))))
#test