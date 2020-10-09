palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis')
vogais = 'aeiou'

for p in palavras:
    print (f'\nNa palavra {p} tem', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')