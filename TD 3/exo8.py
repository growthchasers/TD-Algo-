n = int(input('entrez la valeur de N: '))
if n < 2:
    raise ValueError('N doit entre sup ou égale à 2')
e = 1

for i in range(2, n + 1):
    temp_sum = 0

    for j in range(i, i + 1):
        temp_sum += j

    e *= temp_sum

print(f'La valeur de l expression E est : {e}')