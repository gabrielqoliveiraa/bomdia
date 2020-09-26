from random import randint
c = randint(0, 10)
print('=*'*20)
print('Estou pensando em um número de 0 a 10')
jogador = int(input('Tente adivinhar: '))
count = 1
while jogador != c:
    jogador = int(input('Você errou. Tente novamente: '))
    count += 1

print('Você ganhou ! O número de tentativas para vencer foram {}'.format(count))