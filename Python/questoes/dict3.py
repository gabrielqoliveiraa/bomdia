from datetime import datetime
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
cadastro['idade'] = (datetime.now().year - int(input('Ano de nascimento: ')))
cadastro['ctps'] = int(input('Carteira de trabalho (0 não tem) '))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: R$ '))
    cadastro['aposentadoria'] = (cadastro['contratação']  + 35)
print('-='*30)
for k,v in cadastro.items():
    print(f'{k} tem valor {v}')
  
