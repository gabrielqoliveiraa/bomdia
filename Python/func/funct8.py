def fatorial(num=1, show=False):
    f = 1
    if show == True:
        for c in range(num, 0, -1):
            f = f*c
            print(c, end="") 
            if c > 1: 
                print(' x ', end="")
            else: 
                print(' = ', end="")
        return f
    else:
        for c in range(num, 0, -1):
            f = f*c
        return f

        
        

print(fatorial(5, True))


