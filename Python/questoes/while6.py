razao = int(input('Digite a razão da PA: '))
ftermo = int(input('Digite o primeiro termo: '))
count = 0 
n = 1

while count <= 9:
    count += 1
    termo = ftermo + ((n-1)*razao)
    n += 1
    print(termo, end=' -> ')
    
print('FIM')
            




