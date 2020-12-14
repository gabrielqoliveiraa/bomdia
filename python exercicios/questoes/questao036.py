ValorCasa = float(input('Qual o valor da casa ?'))
Salario = float(input('Qual o seu Salário ? '))
AnosPagar = int(input('Quantos anos pretende pagar ?'))

print('Analisando seu pedido de mepréstimo')
x = (0.3*(Salario))
y = (ValorCasa)/(AnosPagar*12)

if y <= x:
    print('Empréstimo aprovoado')

else:
    print('Empréstimo Negado')