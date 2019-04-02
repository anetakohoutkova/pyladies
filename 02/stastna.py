print('Odpovídej "ano" nebo "ne".')
stastna_retezec = input('Jsi šťastná? ')
if stastna_retezec == 'ano':
    stastna = True
elif stastna_retezec == 'ne':
    stastna = False
else:
    print('Nerozumím!')

print('Odpovídej "ano" nebo "ne".')
bohata_retezec = input('Jsi bohatá? ')
if bohata_retezec == 'ano':
    bohata = True
elif bohata_retezec == 'ne':
    bohata = False
else:
    print('Nerozumím!')


if bohata:
    if stastna:
         print('Gratuluji!')
    else:
         print('Víc usmívat!')
else:
    if stastna:
         print('Šetři!')
    else:
         print('Si v piči!')
