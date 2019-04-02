from math import pi

def obsah_elipsy(a, b):
    return pi * a * b
print(obsah_elipsy(4, 2))


def obvod_obdelnika(sirka, vyska):
    "Vrátí obvod obdelníka daných rozměrů"
    return 2 * (sirka + vyska)

print(obvod_obdelnika(4, 2))

