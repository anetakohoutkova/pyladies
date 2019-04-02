from math import pi


def obsah_elipsy(a, b):
    return pi * a * b
print(obsah_elipsy(4, 2))

def objem_eliptickeho_valce(a, b, vyska):
    return obsah_elipsy(a, b) * vyska
print(objem_eliptickeho_valce(8, 2, 5))