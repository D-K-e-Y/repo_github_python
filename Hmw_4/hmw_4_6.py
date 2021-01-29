###count###

import time
from itertools import count,cycle
user_numb = input('Начальное число: ')
for el in count(int(user_numb)):
    print(el)
    time.sleep(1)
    if el >= 15:
        break

###cycle/FIFO###
import numpy as np
user_numb = input('Введите длину: ')
my_str = np.random.sample(int(user_numb))
new_str = cycle(my_str)
print(my_str)

for i in range(int(user_numb)):
    print(next(new_str))
    time.sleep(1)
#test