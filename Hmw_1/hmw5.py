profits = float(input("Введите сумму выручки фирмы: "))
costs = float(input("Введите сумму издержки фирмы: "))
prof = "Вы в прибыли!"
loss = "Вы в убытке!"
dif = abs(float(profits - costs))
if profits > costs:
    print(prof, "Разница составляет: ", dif)
    pers = int(input("Введите количество сотрудников: "))
    pph = dif / pers # profit per human
    if profits > costs:
        print("Прибыль на одного сотрудника составляет: ", pph)
elif profits == costs:
    print("Вы работаете в ноль!")
else:
    print(loss, "Разница составляет: ", dif)
        