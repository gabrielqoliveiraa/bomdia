contador18 = 0 
contadorMasc = 0 
contadorF = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo: ')).upper().strip()[0]
    if idade >= 18:
        contador18 += 1
    if sexo == 'M':
        contadorMasc += 1
    if sexo == 'F' and idade < 20:
        contadorF += 1
    desejo = ' '
    while desejo not in 'SN':
        desejo = str(input('Deseja continuar ? S/N ')).upper().strip()[0]
    if desejo == 'N':
        break
        

print('Pessoas com mais de 18: {}'.format(contador18))
print('Homens cadastrados: {}'.format(contadorMasc))
print('Mulheres com menos de 20 anos: {}'.format(contadorF))