resposta = 'S'
soma = count = maior = menor = 0
while resposta in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    count += 1
    if count == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        else:
            menor = num

    resposta = str(input('Quer continuar ? S/N ')).upper().strip()[0]


media = soma / count

print('A media foi: {}'.format(media))
print('O maior e menor número foram:{} {} '.format(maior, menor))






    