from time import sleep

def contador(i, f, p):
    print('A)PRIMEIRA CONTAGEM - 1 ATÉ 10 / 1-1')
    if i < f:
        cont = i
        while cont <= f:
            print(f'cont', end=' ')
            sleep(0.5)
            cont += p 


contador(1, 10, 1)


