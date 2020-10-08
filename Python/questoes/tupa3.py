valor1 = int(input('DIgite um valor: '))
valor2 = int(input('Digite um valor: '))
valor3 = int(input('DIgite um valor: '))
valor4 = int(input('DIgite um valor: '))

tupla = (valor1, valor2, valor3, valor4)

if tupla.count(9) == True:
    print(tupla.count(9))

if 3 in tupla:
    print(tupla.index(3))
else:
    print('O valor 3 não foi digitado nenhuma vez')

count = 0 
for c in tupla:
    if c %2 == 0:
        count += 1

print(tupla)
print(count)
