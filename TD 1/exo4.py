# exo 4
print('----------exo4 started---------')

valeur_1 = int(input('entrer un nombre: '))
valeur_2 = int(input('entrer un nombre'))
def exchange(a, b):
    temp = a
    a = b
    b = temp
    print(f'a: {a}\nb: {b}')
    
exchange(valeur_1, valeur_2)

print('----------exo4 finished---------')