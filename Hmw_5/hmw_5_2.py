with open("hmw_5_2.txt") as f:
    lines = 0
    letters = 0
    for line in f:
        lines += line.count("\n")
        letters = len(line)-1
        print(f'Букв в строке: {line} {letters}')
    print(f'\nКоличество строк: {lines}')