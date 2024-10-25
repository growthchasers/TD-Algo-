note = int(input('entre votre note: '))

def mention(note):
    if note < 10:
        return 'Non admis'
    elif 10 <= note < 12:
        return 'Passable'
    elif 12 <= note < 15:
        return 'Assez Bien'
    elif 15 <= note < 18:
        return 'Bien'
    elif 18 <= note:
        return 'Tres Bien'
    else:
        return 'Invalid Note'
    
print(mention(note))