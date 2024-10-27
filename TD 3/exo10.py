n = int(input('entrez la valeur de N: '))

for i in range(1, n + 1):
    for j in range(i):
        print('#', end='')
    print()