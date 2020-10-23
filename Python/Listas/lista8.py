from random import randint
usuario = int(input('Quantos jogos você quer que eu sorteie ? '))
x = []
jg = []



for c in range(0, usuario):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in x:
            x.append(num)
            cont += 1
        if cont >= 6:
            break
    x.sort()
    jg.append(x[:])
    x.clear()
    

for i, l in enumerate(jg):

    print(f'Jogo {i}: {l}')
            
            





