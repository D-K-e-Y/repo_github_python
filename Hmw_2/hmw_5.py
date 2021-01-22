my_list = [10, 8, 5, 4, 4, 3, 3, 3, 2]
print(f"Рейтинг: {my_list}")
num = int(input("Введите число: \nДля завершения введите: '505' "))
while num != 505:
    for el in range(len(my_list)):
        if my_list[el] == num:
            my_list.insert(el + 1, num)
            break
        elif my_list[0] < num:
            my_list.insert(0, num)
        elif my_list[-1] > num:
            my_list.append(num)
        elif my_list[el] > num and my_list[el + 1] < num:
            my_list.insert(el + 1, num)
    print(f"текущий список - {my_list}")
    digit = int(input("Введите число: "))
#test