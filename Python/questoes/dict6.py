cadastrogeral = []
cadastroindiv = {}
listagols = []
listatemp = []
total = 0 

while True:
    cadastroindiv['nome'] = str(input('Nome: '))
    cadastroindiv['partidas'] = int(input('Partidas: '))
    for c in range(0, cadastroindiv['partidas']):
        gols = int(input(f'Quantos gols na partida {c} ?'))
        listatemp.append(gols)
        listagols.append(listatemp[:])
    cadastroindiv['gols'] = listatemp[:]
    cadastroindiv['total'] = sum(listatemp)
    listatemp.clear()
    cadastrogeral.append(cadastroindiv.copy())
    usuario = str(input('Deseja Continuar ? S/N: ')).upper().strip()[0]
    while usuario not in 'SN':
        usuario = str(input('Deseja Continuar ? S/N: ')).upper().strip()[0]
    if usuario == 'N':
        break


print(cadastrogeral)
print('-='*30)
print(f'cod', end=' ')
for i in cadastroindiv.keys():
    print(f'{i:<15}', end='')
print()

for c,v in enumerate(cadastrogeral):
    print(f'{c:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()


        
