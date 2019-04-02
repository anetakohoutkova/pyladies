zaznamy = ["pepa novák", "Jiří Sládek", "Ivo Sládek", "Ivo navrátil", "jan Poledník"]

spravny=[]
nespravny=[]

for zaznam in zaznamy:
    jmeno, prijmeni = zaznam.split()  #nachystám pythonu - jmeno, prijmeni
    #prvek[0], prvek [1] nešikoný zápis
    if not jmeno[0].islower() and not prijmeni[0].islower():
        spravne.append(zaznam)
    print(spravny)
    else:
        spatne.append(zaznam)
        print(spravny)
        print(nespravny)

    #for zaznam in zaznamy:
        #jmeno, prijmeni = zaznam.split()
        #if jmeno[0].islower() or prijmeni()
        #nespravny.append(zaznamy)
    #print(nespravny)








#1 připravit si prázdné seznamy pro správné a nesprávné
#2 projít seznam jmen záznam po záznamu cyklem
#3 zjistit, jestli jméno a příjmení začínájí velkým písmenem
#4 pokud an, přiřadit do seznamu správných záznamů
#5 řešit podobně pro nesprávné záznamy, případně pro opravu záznamů
