# tento program pocita obvod a obsah ctverce

strana = float(input("Zadej cislo"))
cislo_je_spravne = strana > 0
print(cislo_je_spravne)

if cislo_je_spravne:
    print("Obvod ctverce se stranou", strana, "je", strana * 4, "cm")
    print("Obsah ctverce se stranou", strana, "je", strana * strana, "cm2") 
else: 
    print("Zadej kladne cislo.")


print ("Dekuji za pouziti kalkulacky.")