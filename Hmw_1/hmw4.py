n = (int(input("Введите целое положительное число: ")))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    elif n > 9:
        continue
    else:
        print(f"Максимальное цифра в числе: {max}")
        break