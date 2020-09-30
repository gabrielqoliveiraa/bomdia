count = n = 0
while True:
    n = int(input('Digite um número: '))
    while True:
        count += 1
        multi = n*count
        print (f'{n} x {count} = {multi}')
    if n < 0:
        break

 



