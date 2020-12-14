valor = int(input('Digite um valor: '))
ced = 50 
count = 0
total = valor

while True:
    if total >= ced:
        total = total - ced
        count += 1
    else:
        print (f'{count} cédulas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if total == 0:
            break
            

