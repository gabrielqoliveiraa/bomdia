idade = int(input('Quantos anos você tem ?'))

if idade > 18:
    b = idade - 18
    print('Você preciisa se alistar pois está atrasado {} anos'.format(b))

elif idade < 18:
    b = 18 - idade
    print('Você deve aguardar para se alistar, faltam {} anos'.format(b))
else:
    print('Você está na idade certa para alistar')