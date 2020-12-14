primeiroValor = int(input('Digite um primeiro Valor'))
segundoValor = int(input('Digite um segundo Valor'))

if primeiroValor > segundoValor:
    print('O {} é maior que {}'.format(primeiroValor, segundoValor))
elif segundoValor > primeiroValor:
    print('O valor {} é maior que {}'.format(segundoValor,primeiroValor))
else:
        print('Os valores são iguaiis')
   