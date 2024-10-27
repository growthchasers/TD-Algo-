n = int(input('entrez un entier N: '))
facteurs = []

for i in range(1,  int(n**0.5) +1):
    if n % i == 0:
        facteurs.append(i)
        if i != n // i:
            facteurs.append(n // i)
facteurs.sort()
print(f'Les Facteurs de {n} sont: {facteurs}')