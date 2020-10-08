numero = ('Zero','Um', 'Dois', 'Tres', 'Quatro', 'Cinco','Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quartorze', 'Quinze','Dezesseis', 'Dezessete','Dezoito', 'Dezenove', 'Vinte')

while True:
    resp = int(input('Digite um número entre 0 e 20: '))
    while resp > 20 or resp < 0:
        resp = int(input('Tente Novamente. Digite um número de 0 a 20: '))
    print (numero[resp])
    usuario = str(input('Deseja continuar S/N ? ')).upper().strip()[0]

    if usuario == 'N':
        break




    


print("Obrigado")

    


   


