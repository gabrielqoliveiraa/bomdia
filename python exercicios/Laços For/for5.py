a = int(input('Digite um numero '))
count = 0
for c in range (1, a+1):

    if a % c == 0:
        count += 1
        print('Ele é divísivel por', c)
if count == 2:
        print('Esse número é primo')
        pass


#print(c, end=' ')
     