print('=*'*20)
print('SEQUÊNCIA DE FIBONACCI')
print('=*'*20)
a = int(input('Digite o número de elementos da sequencia que você quer ver: '))
count = 3
termo1 = 0
termo2 = 1
print(termo1, termo2, end=' -> ')

while count <= a:
    termo3 = termo1 + termo2
    print(termo3, end=' ')
    termo1 = termo2
    termo2 = termo3

print('FIM')
    

     
