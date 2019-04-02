domaci = ["pes", "kočka", "králík", "had", "andulka"]
pomocny = []
vysledny = []

for zvire in domaci:
    dvojice = (zvire[1], zvire)
    pomocny.append(dvojice)
pomocny.sort()

vysledny = [zvire for i, zvire in pomocny]
print(vysledny)


#list comprehention
#for i, zvire in pomocny:
#vysledny.append(zvire)
#print(vysledny)
