tuplanome = ('Shampoo', 8.50, 
            'Condicionador', 12.50, 
            'Balão', 3.50,
            'Tiara', 4.50)
print('-'*50)
print('Listagem de Preço'.center(50))
print ('-'*50)


for c in range(0, len(tuplanome)):
    if c % 2 == 0:
        print(f'{tuplanome[c]:.<30}', end='')
    else:
        print (f'R$ {tuplanome[c]}')

