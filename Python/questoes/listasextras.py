listageral = []
listapar = []
listaimpar = []

while True:
    usuario = int(input('Digite um numero: '))
    if usuario % 2 == 0:
        listageral.append(usuario)
        listapar.append(usuario)
    else:
        listageral.append(usuario)
        listaimpar.append(usuario)
    usuarioResp = str(input('Deseja continuar ? ')).upper().strip()[0]
    if usuarioResp == 'N':
        break

listageral.sort()
listapar.sort()
listaimpar.sort()

print('A lista com todos os elementos gerados é {}'.format(listageral))
print(f'A lista apenas com os PARES é {listapar}')
print('A lista com os impares é: ',listaimpar)