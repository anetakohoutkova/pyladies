rodne_cislo = input("Napiš rodné číslo.")

slovnik_spravnosti = {True: "je", False: "není"}

def je_zena_nebo_muz(rodne_cislo):
    return "píča" if rodne_cislo[2] == "5" else "penis"

def ma_spravny_format(rodne_cislo):
    if "/" not in rodne_cislo:
        return False

    pred, za = rodne_cislo.split("/")
    return len(pred) == 6 and len(za) == 4

def je_spravne_delitelne(rodne_cislo):
    return int(rodne_cislo[:6] + rodne_cislo[7:]) % 11 == 0

if len(rodne_cislo) == 11:

    spravny_format = ma_spravny_format(rodne_cislo)
    delitelnost_11 = je_spravne_delitelne(rodne_cislo)
    pohlavi = je_zena_nebo_muz(rodne_cislo)
    datum_narozeni = [rodne_cislo[:2], rodne_cislo[2:4], rodne_cislo[4:6]]

    print("Vaše rodne_cislo {} ve správném formátu. RČ {} dělitelné 11. Vaše datum narození {}. Vaše pohlaví je {} .".format(
        slovnik_spravnosti[spravny_format], slovnik_spravnosti[delitelnost_11], datum_narozeni, pohlaví))

else:
    print("Nezadal jsi správně!")
