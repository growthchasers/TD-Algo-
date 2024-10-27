chars = []
for i in range(250):
    char = input(f'entre le character {i}: ' )
    if char == '.':
        break
    elif len(char) > 1:
        raise ValueError('entrez juste une charactere')
    else:
        chars.append(char)

count = 0
for i in chars:
    if i == 'a':
        count += 1
print(f'le character a se repete {count} fois')
