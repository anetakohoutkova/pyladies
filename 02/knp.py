tah_pocitace = 'kámen'
tah_cloveka = input('kámen, nůžky, nebo papír? ')

if tah_pocitace == tah_cloveka:
    print ('Plichta.')
elif (tah_pocitace == 'nůžky' and tah_cloveka == 'kámen') or (tah_pocitace == 'kámen' and tah_cloveka == 'papír') or (tah_pocitace == 'papír' and tah_cloveka == 'nůžky'):
    print ('Vyhrála jsi.')
elif (tah_pocitace == 'kámen' and tah_cloveka == 'nůžky') or (tah_pocitace == 'papír' and tah_cloveka == 'kamen') or (tah_pocitace == 'nůžky'and tah_cloveka == 'kámen'):
    print ('Prohrála jsi.')
else:
    print('Nerozumím.')