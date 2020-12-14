from random import randint
from time import sleep

def sorteio(lista):
    for c in range(0,5):
        c = randint(1, 10)
        lista.append(c)
    print('Valores Sorteados: ')
    for c in lista:
        print (f'{c}', end= ' ', flush=True)
        sleep(0.5)

def somaPar(lista):
    a = 0 

    print('Soma dos Valores Pares: ')
    for c in lista:
        if c % 2 == 0:
            a = a + c 
    print (f'{a}', end= ' ', flush=True)

        
        
       




num = list()
sorteio(num)
somaPar(num)