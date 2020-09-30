from random import randint
n = soma = count = 0
while True:
    lista = randint(1, 10)
    n = int(input('Digite um numero: '))
    escolha = str(input('Par ou Impar ? I/P: ')).upper().strip()[0]
    soma = n + lista
    count += 1
    if escolha == 'P' and soma % 2 == 0:
        print(f'O computador jogou {lista} A Soma deu {soma} deu Par')
        print('Voce ganhou')
    elif escolha == 'I' and soma % 2 != 0:
        print(f'O computador jogou {lista} A Soma deu {soma} deu Impar')
        print('Voce ganhou')
    else:
        print(f'O computador jogou {lista} A Soma deu {soma}')
        break

print ('Acabou o jogo !! Você ganhou {} vezes'.format(count))

  
    