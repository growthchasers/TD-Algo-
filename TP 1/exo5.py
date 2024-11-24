entiers = []

for i in range(1, 4):
    entier = int(input(f'entrez le nombre {i}: '))
    entiers.append(entier)
      
max_entier = entiers[0]
min_entier = entiers[0]

for i in entiers[1:]:
    if i > max_entier:
        max_entier = i
    if i < min_entier:
        min_entier = i
        
print(f'le minimum entier est: {min_entier} ')
print(f'le maximum entier est: {max_entier} ')