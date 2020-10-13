numeros = list()

for c in range(0,5):
    numeros.append(int(input('Digite um numero: ')))
    if numeros[c] > numeros[c-1]:
        numeros[c] = numeros[c+1]

print(numeros)