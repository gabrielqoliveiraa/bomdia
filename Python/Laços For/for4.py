print('Os 10 primeiros termos de uma PA são: ')
n = 1
first = int(input('Digite o primeiro Numero '))
razao = int(input('Digite a razão '))
decimo = first + (11-1)*razao
for c in range (first, decimo, razao):
    print(c)
