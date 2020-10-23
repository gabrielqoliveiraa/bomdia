aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    print('Situação: Aprovado ')
else:
    print('Reprovado!')

for k, v in aluno.items():
    print(f'{k} é igual a {v}')


