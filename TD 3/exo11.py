n = int(input('entrez la valeur de N: '))

one_position = 0
for i in range(n):
    for j in range(n):
        if j == one_position:
            print('1', end='')
        else:
            print('0', end='')
    one_position += 1
    print()