x = int(input('Digite um número: '))
print('Escolha uma opção de conversão: \n 1 - Binário \n 2 - Octal \n 3 - Hexadecimal')
j = int(input('Para qual base você quer transformar esse número ? '))

if j == 1:
    print('O seu número em binário é {}'.format(bin(x)[2:]))
elif j == 2:
     print('O seu número em Octal é{}'.format(oct(x)[2:]))
     pass
elif j == 3:
     print('O seu número em Hexa é {}'.format(hex(x)[2:]))
     pass

