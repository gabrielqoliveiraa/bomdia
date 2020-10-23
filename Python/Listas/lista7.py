geral = [[], []]
usuario = 0 

for c in range(1,8):
    usuario = int(input(f'Digite o {c} valor: '))
    geral.append(usuario)
    if usuario % 2 == 0:
        geral[0].append(usuario)
    else:
        geral[1].append(usuario)

geral[0].sort()
geral[1].sort()
print(f'Os números pares digitados foram: {geral[0]}')
print(f'Os números impares digitados foram: {geral[1]}')





