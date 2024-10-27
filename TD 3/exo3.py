a = int(input('entrez le dividende: '))
b = int(input('entrez le diviseur: '))

if b == 0:
    raise ValueError('la division par 0 pas définie')
quotient = 0
reste = abs(a)

while reste >= abs(b):
    reste -= abs(b)
    quotient += 1

if (a < 0) != (b < 0):
    quotient = -quotient
if a < 0:
    reste = - reste

print(f'Quotient : {quotient}\nReste: {reste}')