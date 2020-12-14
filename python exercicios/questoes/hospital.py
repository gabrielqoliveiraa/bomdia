#Gestor de Visitas






#Programa Principal
pacientes = {}
listatempnome = list()
listatempidade = list()

while True:
    listatempnome.append(input('Nome: '))
    listatempidade.append(input('Idade: '))
    pacientes['nome'] = listatempnome[:]
    pacientes['idade'] = listatempidade[:]
    listatempidade.clear
    listatempnome.clear
    sair = int(input('999: '))
    if sair == 999:
        break

print(pacientes)
