numeros =  []

while True:
    numeros.append(int(input('Digite um numero: ')))
    usuario = str(input('Deseja continuar ? S/N: ')).upper().strip()[0]
    if usuario == 'N':
        break
    

print(f'A quantidade de números da sua lista é de {len(numeros)}')
numeros.sort(reverse = True)
print(f'A sua lista ordenada é {numeros}')
print (f'O número 5 está na lista foi digitado {numeros.count(5)} vez')





