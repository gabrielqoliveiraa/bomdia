numeros = list() #[]

while True:
    a = (int(input('Digite um número: ')))
    if a not in numeros:
        print('Valor adicionado com sucesso!')
        numeros.append(a)
    else:
        print('Valor duplicado !')
    usuario = str(input('Quer continuar ? S/N ')).upper().strip()
    if usuario == 'N':
        break


print(numeros)