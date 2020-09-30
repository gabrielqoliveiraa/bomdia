count = n = 0
while True:
    n = int(input('Digite um número: '))
    if n < 0:
            break
    for count in range(0,10):
        count += 1
        multi = n*count
        print (f'{n} x {count} = {multi}')
        
print('Você digitou um número inválido')

 



