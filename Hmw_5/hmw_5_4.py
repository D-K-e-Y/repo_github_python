replacements = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
result = []
with open("hmw_5_4.txt", 'r') as f:
    for line in f:
        tokens = line.split(' ', 1)
        if tokens[0] in replacements:
            word = replacements[tokens[0]]
            result.append(word + ' ' + tokens[1])
    print(result)
with open('hmw_5_4_test.txt', 'w') as f:
    f.writelines(result)