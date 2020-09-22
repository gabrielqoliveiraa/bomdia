from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
lista1 = randint(0, 2)
print(' 0 - PEDRA \n 1 - PAPEL \n 2 - TESOURA')
opcoes = int(input('Escolha uma sua jogada: '))
print('JO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PO')
print('-='*11)
print ('O jogador jogou {}'.format(itens[opcoes]))
print ('O computador jogou {}'.format(itens[lista1]))
print('-='*11)
if opcoes == lista1:
    print ('EMPATE')

elif (opcoes == 0 and lista1 == 2) or (opcoes == 1 and lista1 == 0) or (opcoes == 2 and lista1 == 1):
    print ('O jogador ganhou')

else:
    print ('O jogador perdeu')




    



