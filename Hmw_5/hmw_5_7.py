import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('hmw_5_7.txt', 'r') as file:
    for line in file:
        name, firm, earning, costs = line.split()
        profit[name] = int(earning) - int(costs )
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Средняя прибыль: {prof_aver}')
    else:
        print(f'Вы в убытке.')
    pr = {'Средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')