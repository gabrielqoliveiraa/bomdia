primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
count = 1
termo = primeiro

while count <= 11:
    termo = termo + razao
    count += 1
    print(termo, end= ' ')
    if count == 10:
        escolha = int(input('Você deseja continuar ? \n 1 - Sim \n 2 - Não'))
        if escolha == 1:
            escolha1 = int(input('Até qual termo ? '))
            while count <= escolha1:
                termo = termo + razao
                print('Sua nova PA É:')
                print(termo, end=(' '))
            
            




