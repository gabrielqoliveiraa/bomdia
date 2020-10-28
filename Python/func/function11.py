def notas(*num):
    num = {}
    maior = menor = 0
    count = 0
    for c in num:
        if count == 0:
            maior = num[0]
            menor = num[0]
        else:
            if num[c] > maior:
                maior = num[c]
            elif num[c] < menor:
                menor = num[c]
        count += 1
    soma = sum(num)
    num['media'] = soma/len(num)
    num['maior'] = maior
    num['menor'] = menor 
    num['total'] = len(num)
    return num





resp = notas(4.5, 4, 8, 9)
print(resp)
        
