nome = []
temp = []
pesoMaior = pesoMenor = 0
count = 1


while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if count == 1:
        pesoMaior = pesoMenor = temp[1]
    else:
        if temp[1] >= pesoMaior:
          pesoMaior = temp[1]
        elif temp[1] <= pesoMenor:
            pesoMenor = temp[1]
    nome.append(temp[:])
    temp.clear()
    usuario = 'O'
    while usuario != 'S' or usuario != 'N':
        usuario = str(input('Deseja Continuar ? S/N: ')).upper().strip()[0]
        if usuario == 'S':
            break
        elif usuario == 'N':
            break
    if usuario == 'N':
        break
    count += 1


print(f'Foram cadastradas {len(nome)} pessoas')
print(f'O menor peso foi {pesoMenor}.', end=' ')
for c in nome:
    if c[1] == pesoMenor:
        print(c[0], end=' ')
print()
print(f'O maior peso foi {pesoMaior}.')
for c in nome:
    if c[1] == pesoMaior:
        print(c[0])
            
          
       

    

    

    
    


    


    
    
    
