count17 = 0
count18 = 0 
for c in range (0,8,1):
    a = int(input('Digite uma idade: '))
    if a >= 18:
        count18 = count18 + 1
    else:
        count17 = count17 +1

print('A quantidade de poessoas com maior de 18 anos é: {}'.format(count18))
print('A quantidade de poessoas com menor de 18 anos é: {}'.format(count17))

