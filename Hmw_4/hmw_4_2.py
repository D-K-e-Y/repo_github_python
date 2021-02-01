my_list = [3, 5, 27, 17, 14, 21, 72, 100, 256, 6, 18]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(my_list)
print(my_new_list)