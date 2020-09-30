soma = mais1000 = 0 
maisbarato = 0

while True:
    nome = str(input('Digite o nome: '))
    preco = float(input('Digite um preço: '))
    soma += preco
    if preco > 1000:
        mais1000 += 1
    elif preco > maisbarato:
        maisbarato = nome
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Deseja Continuar ? S/N:' )).upper().strip()[0]
    if resp == 'N':
        break 
print(f'O total gasto foi de {soma}')
print(f'{mais1000} Produtos custam mais de 1000')
print (f'O produto mais barato é {maisbarato}')

