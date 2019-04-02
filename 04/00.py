domaci = ["pes", "kočka", "králík", "had"]

krátké = []

for zvire in domaci:
    if len(zvire) < 5:
        print(zvire)
        krátké.append(zvire)

print (krátké)


