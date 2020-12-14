def ficha(nome='deconhecido' , gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato')
   



nomeUsuario = str(input('Nome Jogador:'))
golsUsuario = str(input('Gols: '))
if golsUsuario.isnumeric():
    golsUsuario = int(golsUsuario)
else:   
    golsUsuario = 0
if nomeUsuario.strip() == '':
    ficha(gols=golsUsuario)
else:
    ficha(nomeUsuario, golsUsuario)
