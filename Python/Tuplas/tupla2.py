from random import randint
tupla = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
maior = 0
menor = 0

for c in tupla:
    print(c, end= ' ')
print(f'O maior foi {max(tupla)}')
print(f'O menor foi {min(tupla)}')


    



