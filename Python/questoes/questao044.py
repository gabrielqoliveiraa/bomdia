Valor = float(input('Qual o valor do seu produto ? '))
print('''Formas de pagamento do produto:'
1 - A vista DN (10% de desconto)
2 - A Vista Cartão (5% de desconto)
3 - 2x Cartão (Sem desconto)
4 - 3x Mais (20% Juros) ''')
PagamentoSelecionado = int(input('Qual forma gostaria de pagar '))

if PagamentoSelecionado == 1:
    A = Valor*0.9
    print('Seu desconto foi de 10% e o valor do produto é R$', A)

elif PagamentoSelecionado == 2:
    A = Valor*0.95
    print('Seu desconto foi de 5% e o valor do produto é R$', A)

elif PagamentoSelecionado == 3:
    print('Você não obteve desconto e o valor do produto é', Valor)

elif PagamentoSelecionado == 4:
    A = Valor*1.2
    print('Seu juros foi de 20% e o valor do produto é R%', A)