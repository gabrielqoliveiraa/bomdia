ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
count = 0
quantidadeTermos = 10

while count <= quantidadeTermos:
    ptermo += razao
    count += 1
    print(ptermo, end=' ')
    if count == quantidadeTermos:
        escolha = int(input('\n Quantos termos você quer a mais ? '))
        quantidadeTermos = escolha + count
        if escolha == 0:
            exit()
print('FIM')


    

    




