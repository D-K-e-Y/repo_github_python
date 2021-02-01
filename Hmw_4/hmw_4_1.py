def wage():
    try:
        work_time = float(input("Введите отработанное время: "))
        hour_wage = float(input("Введите размер платы за 1 час: "))
        bonus = float(input("Введите размер премии: "))
        am_wage = (work_time * hour_wage) + bonus
        print(float((am_wage)))
    except:
        print("Что-то не так. Введите правильные данные.")
wage()