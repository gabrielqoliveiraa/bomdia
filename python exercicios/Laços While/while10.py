n = soma = count = 0
while True:
    n = int(input('Digite um numero [999 para para]: '))
    if n == 999:
        break
    soma += n
    count += 1


print(f'O valor da soma é {soma}')
print(f'A quantidade de números foi {count}')
