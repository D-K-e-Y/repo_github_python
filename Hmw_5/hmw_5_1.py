f = open('data.txt', 'tw+')
data = input('Введите данные: ')
while data:
    f.writelines(data)
    data = input('Введите данные: ')
    if not data:
        break
result = f.readlines()
print(result)
f.close()