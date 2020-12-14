lista = []
temp = []

while True:
    temp.append(str(input('Nome: ')))
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    media = (nota1+nota2)/2
    usuario = ' '
    temp.append(media)
    temp.append(nota1)
    temp.append(nota2)
    while usuario not in 'SsNn':
        usuario = str(input('Quer continuar ? S/N: ').upper().strip())[0]
    lista.append(temp[:])
    temp.clear()
    if usuario == 'N':
        break

print('-='*30)
print(f'{"No":<4} {"NOME":<10} {"MEDIA":>8}')
print('-'*26)

for c,v in enumerate(lista):
    print(f'{c:<4} {v[0]:<10} {v[1]:>8}')

while True:
    notas = int(input('Você deseja mostrar as notas de qual aluno ? (999 interrompe): '))
    if notas == 999:
        break
    print(f'Notas de {lista[notas][0]} são {lista[notas][2:]}')

    
    


   
    

    