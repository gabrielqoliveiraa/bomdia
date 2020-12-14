





#Programa principal 
profissoes = ['Enfermeiro', 'Garçom', 'Médico', 'Caixa']
precos = [15.40, 8.70, 22.30, 12.20]

print('Essas são as profissões:')
for c,v in enumerate(profissoes):
    print(f'--> {c:<3} {v:<3} ==  R$ {precos[c]:>4}')

escolhaUsuario = int(input('Digite o código de uma: '))

while escolhaUsuario > (len(profissoes)-1):
    escolhaUsuario = int(input('ERRO ! Digite um código válido: '))

print(f'Você escolheu {profissoes[escolhaUsuario]}')

while True:
    horasExtras = float(input('Horas extras: '))
    salarioFixo = float(input('Salário: '))
    salarioTotal = (horasExtras*precos[escolhaUsuario]) + salarioFixo
    print(f'Seu salário esse mês foi de: {salarioTotal}')
    print('-='*30)
    continuaUsuario = str(input('Deseja continuar (S/N) ?: ')).upper().strip()[0]
    while continuaUsuario not in 'SN':
        continuaUsuario = str(input('Digite uma opção válida ! S/N'))
    if continuaUsuario == 'N':
        break
