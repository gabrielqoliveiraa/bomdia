def menu(texto):
    print('=-'*30)
    print(texto)
    print('=-'*30)






#Programa Principal
profissoes = []
preco = []
menu('CADASTRO')
while True:
    profissoes.append(input('Profissão: '))
    preco.append(float(input('Valor da Hora: ')))
    continuaUsuario = str(input('Deseja Continuar S/N ? ')).upper().strip()[0]
    while continuaUsuario not in 'SN':
        continuaUsuario = str(input('Deseja Continuar S/N ? ')).upper().strip()[0]
    if continuaUsuario == 'N':
        break

menu('MENU DE PROFISSÕES CADASTRADAS')


while True:
    for c,v in enumerate(profissoes):
        print(f'--> {c:>4} {v:>4} --------------- R$ {preco[c]}')

    escolhaUsuario = str(input('Qual profissão deseja calcular: '))
    int(escolhaUsuario)
    if escolhaUsuario > (len(profissoes) - 1):
        escolhaUsuario = int(input('ERRO ! Digite um código válido: '))
    salarioFixo = float(input('Valor fixo: '))
    horasExtras = float(input('Horas Extras: '))
    salarioTotal = salarioFixo + (horasExtras*preco[escolhaUsuario])
    print()
    print(f'SALÁRIO DO {profissoes[escolhaUsuario]} FOI DE: {salarioTotal}')
    continuaUsuario2 = str(input('Deseja Continuar S/N ? ')).upper().strip()[0]

    while continuaUsuario2 not in 'SN':
        continuaUsuario2 = str(input('Deseja Continuar S/N ? ')).upper().strip()[0]
    if continuaUsuario2 == 'N':
        break

