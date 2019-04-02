krok = int(input('Kolik ujdeš kroků za den?'))
if krok >= 30000:
    print('To si bezel maraton?')
elif krok >= 10000:
    print('Si cvivil?')
elif krok >= 5000:
    print('Prumerna klasika za den.')
elif krok >= 0:
    print('Ziješ?')
else:
    print('Nerozumim zadani')