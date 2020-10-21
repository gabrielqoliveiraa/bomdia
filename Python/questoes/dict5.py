cadastro = list()
idade = 0

while True:
    nome = str(input('Nome: '))
    dict_usuario = dict()
    dict_usuario['nome'] = nome
    sexo = str(input('Sexo: ')).upper().strip()[0]
    while sexo not in 'MF':
        print('ERRO! DIGITE APENAS M OU F')
        sexo = str(input('Sexo: ')).upper().strip()[0]
    dict_usuario['sexo'] = sexo
    dict_usuario['idade'] = int(input('Idade: '))
    cadastro.append(dict_usuario)
    usuario = str(input('Continuar ? S/N: ')).upper().strip()[0]
    idade = (idade + dict_usuario['idade']) 
    while usuario not in 'SN':
        print('ERRO! Digite apenas S ou N')
        usuario = str(input('Continuar ? S/N: ')).upper().strip()[0]
    if usuario == 'N':
        break 

        

media = idade/len(cadastro)
print(f'O grupo tem {len(cadastro)} pessoas')
print(f'A média de idade é de {media:5.2f}')
print(f'A lista de mulheres cadastras é: ', end='')
for p in cadastro:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end=' ')
print()
print(f'As pessoas acima da media: ')
for p in cadastro:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')


print(cadastro)





