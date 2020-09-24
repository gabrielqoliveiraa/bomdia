valorBaseMax = 0
ValorBaseMin = 0
for c in range (0, 5,):
    a = float(input('Digite um peso: '))
    if c == 0:
        ValorBaseMin = a
        valorBaseMax = a
    else:
        if a > valorBaseMax:
            valorBaseMax = a
        if a < ValorBaseMin:
            ValorBaseMin = a

print(valorBaseMax)
print(ValorBaseMin)        
            



        


    