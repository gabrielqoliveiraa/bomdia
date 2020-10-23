idadebase = 0
idade2 = 0
hMax = ''
hiiMax = 0 
countMulher = 0

for c in range(1, 4):
    idadebase += 1
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu Sexo: M OU F ')
    idade2 = idade2 + idade
    if idadebase == 3:
       idade2 = idade2/3
    if c == 1:
        hMax = nome
        idade = hiiMax
    else:
        if idade > hiiMax and sexo in 'Mm':
            nome = hMax
            idade = hiiMax
    if idade < 18 and sexo in 'Ff':
        countMulher += 1




print('{:.2f}'.format(idade2))
print(hMax)
print(countMulher)
    

        


        
