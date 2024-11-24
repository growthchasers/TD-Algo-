somme = 0
produit = 1

for i in range(1, 4):
    nombre = int(input(f'entrez le nombre {i}: '))
    somme += nombre
    produit *= nombre
    
moyenne = somme / 3
print(f'Somme: {somme}')
print(f'Produit: {produit}')
print(f'Moyenne: {moyenne}')