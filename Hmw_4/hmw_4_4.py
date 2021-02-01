my_list = [7, 8, 8, 8, 9, 12, 11, 72, 35, 11, 11, 17, 8, 26]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_list)
print(my_new_list)