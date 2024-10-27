x = int(input('entrez un entier x: '))
diviseurs = []
for i in range(1, x + 1):
    if x % i == 0:
        diviseurs.append(int(i))
    
print(diviseurs)