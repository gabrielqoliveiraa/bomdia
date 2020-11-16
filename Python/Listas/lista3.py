numeros = list()

for c in range(0,5):
    u = int(input('Digite um numero: '))
    if c == 0 or u > numeros[-1]:
        numeros.append(u)
    else:
        quarry = 0
        while quarry < len(numeros):
            if u <= numeros[quarry]:
                numeros.insert(quarry, u)
                quarry += 1
                break

print(numeros)
