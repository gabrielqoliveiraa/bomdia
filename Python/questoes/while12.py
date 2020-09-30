from random import randint
n = soma = 0 
lista = randint(1, 2)
while True:
    n = int(input('Digite um numero: '))
    escolha = str(input('Par ou Impar ? I/P: ')).upper().strip()[0]
    soma = n + lista
    if escolha == 'P' and soma % 2 == 0:
        print(f'O computador jogou {lista} A Soma deu {soma} deu Par')
        print('Voce ganhou')
    elif escolha == 'I' and soma % 2 != 0:
        print(f'O computador jogou {lista} A Soma deu {soma} deu Impar')
        print('Voce ganhou')
    else:
        print(f'O computador jogou {lista} A Soma deu {soma}')
        break

print ('Acabou o jogo !! Você perdeu')

  
    