domaci = ["pes", "kočka", "králík", "had"]
divoký = ["prase", "veverka", "jezevec", "had"]

obe = []
prvni = []
druhy = []

for zvire in domaci:
    if zvire in divoký:
        obe.append(zvire)
    else:
        prvni.append(zvire)

for zvire in divoký:
    if zvire not in  domaci:
        druhy.append(zvire)

print(obe)
print(prvni)
print(druhy)