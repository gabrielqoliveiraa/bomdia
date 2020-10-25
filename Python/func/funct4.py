from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1


    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            #sleep(0.4)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ') 
            #sleep(0.4)
            cont -= p
        print('FIM')

contador(1, 10, 1)
contador(10, 0, 2)
inicioUsuario = int(input('INICIO: '))
fimUsuario = int(input('FIM: '))
passoUsuario = int(input('PASSO: '))
contador(inicioUsuario, fimUsuario, passoUsuario)

    





