valor1 = int(input('Valor 1: '))
valor2 = int(input('Valor 2: '))
jogada = 0
maiorValor = 0

while jogada != 5:
    print(' 1 - somar \n 2 - multiplicar \n 3 - maior \n 4 - novos números \n 5 - sair')
    jogada = int(input('Digite sua jogada: '))
    if jogada == 1:
        a = valor1 + valor2
        print(a)
        StopIteration
    elif jogada == 2:
        a = valor1*valor2
        print(a)
    elif jogada == 3:
        if valor1 > valor2:
            maiorValor = valor1
        else:
            maiorValor = valor2
        print(maiorValor)
    elif jogada == 4:
        print ('Digite novos números')
        valor1 = int(input('Valor 1: '))
        valor2 = int(input('Valor 2: '))   



