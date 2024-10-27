n = int(input('entrez un entier n: '))
for i in range(2, n):
    if n % i == 0:
        print(f'Le nombre {n} est pas premier')
        break
else:
    print(f'Le nombre {n} est premier')