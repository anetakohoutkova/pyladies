košík = {"jablko": "červené", "hruška": "zelená", " broskev": "oranžová", "banán": "žlutý"}

shnilý_košík={}

for ovoce, barva in košík.items():
    shnilý_košík[ovoce]= "hnědo-{}".format(barva)

print(shnilý_košík)

#()metody
#[]index, poloha - obal listu
#{} obal slovníku - předpřipravený
