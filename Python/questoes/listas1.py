numeros = []
maior = menor = 0

for c in range(0,5):
    numeros.append(int(input('Digite um número: ')))
    if c == 0:
     maior = menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]

print('Você digitou os números: ', numeros)


for c, v in enumerate(numeros):
    if v == maior:
     print (f'O maior número é {maior} e sua posição é {c}') 
    if v == menor:
        print (f'O menor número é {menor} e sua posição é {c}')


print(maior)
print(menor)


