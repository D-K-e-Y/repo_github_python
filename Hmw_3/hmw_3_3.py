def my_func (a, b, c):
    if a >= b and b >= c:
        print(f'Наибольшие числа:{a, b}')
        return a + b
    elif b >= a and c>=a:
        print(f'Наибольшие числа:{b, c}')
        return b + c
    elif a >= a and c>=b:
        print(f'Наибольшие числа:{a, c}')
        return a + c
print(f'Сумма: {my_func(int(input("Введите число:")), int(input("Введите число:")), int(input("Введите число:")))}')
#test