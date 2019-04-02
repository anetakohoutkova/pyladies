rc = input("Napiš rodné číslo.")

spravny_format = None
delitelnost_11 = None
datum_narozeni = None
pohlavi = None
slovnik_spravnosti = {True: "je", False: "není"}


if len(rc) == 11:
    if "/" in rc:
        pred, za = rc.split("/")
        if len(pred) == 6 and len(za) == 4: 
            spravny_format = True
    else:
        spravny_format = False

    if int(rc[:6] + rc[7:]) % 11 == 0:
        delitelnost_11 = True
    else:
        delitelnost_11 = False

    datum_narozeni = [rc[:2], rc[2:4], rc[4:6]]

    if rc[2] == "5":
        pohlavi = "piča"
    else:
        pohlavi = "penis"


    print(("Vaše rc {} ve správném formátu. RČ {} dělitelné 11. Vaše datum narození {}. Vaše pohlaví je {} .").format(
        slovnik_spravnosti[spravny_format], slovnik_spravnosti[delitelnost_11], datum_narozeni, pohlavi))

else:
    print("Nezadal jsi správně!")


