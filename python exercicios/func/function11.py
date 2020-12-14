def notas(*num, sit=False):
    r = dict()
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['média'] = sum(num)/len(num)

    return r





resp = notas(4.5, 4, 8, 9)
print(resp)
        
