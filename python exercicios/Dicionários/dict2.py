from random import randint
from time import sleep
from operator import itemgetter
ranking = {}
jogo = {}
a = 0



for c in range(1, 5):
    a = randint(1, 6)
    jogo[f'jogador{c}'] = a

for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse = True)    
print('O RANKING FOI ')
for i,v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
    






