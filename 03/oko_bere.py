from random import randrange
body = 0

print("Počet bodů:",body)
while (body < 21):
     odpoved = input('Mám otočit kartu?')
     if odpoved == 'ano':
          karta = randrange(2, 11)	   
          body = body + karta
          print('Body:',body)
     elif odpoved == "ne":
          print('Body:',body)
          break
     else:
          print('Nerozumím?')

if body <= 21:
     print("SUPER")
elif body > 21:
     print("Prohrál jsi!!!")
