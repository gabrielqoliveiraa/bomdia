geral = {}
aproveitamento = list()
geral['nome'] = str(input('Nome jogador: '))
partidas = int(input(f'Quantas partidas {geral["nome"]} jogou ?'))
count = 0
total = 0 
while count < partidas:
    gols_games = (int(input(f'Quantos gols na partida {count}?')))
    aproveitamento.append(gols_games)
    total = total + gols_games
    count +=1
geral['gols'] = aproveitamento[:]
geral['total'] = total
print('-='*30)
print(geral)
print('-='*30)
for k,v in geral.items():
    print(f'o campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {geral["nome"]} jogou {count} partidas')
i = 0
count2 = 0
for c in aproveitamento:
    print(f' {"=>":>5} Na partida {count2+1}, fez {geral["gols"][i]}')
    i +=1
    count2 +=1



