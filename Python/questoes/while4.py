n = int(input('Digite um número: '))
c = n
fatorial = 1
while c > 0:
    print(c, end=' ')
    fatorial = c * fatorial
    c -= 1


print(fatorial)