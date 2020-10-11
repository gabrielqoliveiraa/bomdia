lista1 = list()
valorMaior = valorMenor = 0

for v in range(0,5):
    lista1.append(int(input('Digite um valor: ')))
    if v == 0:
        valorMaior = valorMenor = lista1[v]
    else:
        if lista1[v] > valorMaior:
            valorMaior = lista1[v]
        else:
            valorMenor = lista1[v]


print(f'A lista é {lista1}')
print(f'O maior valor é {valorMaior} na posição', end=' ')

for c, a in enumerate(lista1):
    if a == valorMaior:
        print(f'{c}')

print(f'O menor valor é {valorMenor} na posição', end=' ')
    
for c, a in enumerate(lista1):
    if a == valorMenor:
        print(f'{c}', end=' ')

        


        
   
