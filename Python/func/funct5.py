def maiorv(*num):
    maior = cont = 0 
    for c in num:
        if cont == 0:
            maior = c
        else:
            if cont > maior:
                maior = c
        cont += 1
    print(maior)



maiorv(3,4,5,6,7,1,1,5)
    
