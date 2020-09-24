idadebase = 0
hMax = ''
hiiMax = 0 

for c in range(1, 4):
    idadebase += 1
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu Sexo: M OU F ')
    if idadebase == 3:
       idade/3
    if c == 1:
        hMax = nome
        idade = hiiMax
    else:
        if idade > hiiMax:
            nome = hMax
            idade = hiiMax

print(idade)
print(hMax)
    

        


        
