from time import sleep

def contador(i, f, p):
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(1)
            cont += p
    
contador(1, 10, 1)

    





