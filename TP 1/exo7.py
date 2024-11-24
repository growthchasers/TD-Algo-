# palindrome numbers

number = input('entrez un nombre: ')

if number == number[::-1]:
    print('Vrai')
    exit()
print('Faux')