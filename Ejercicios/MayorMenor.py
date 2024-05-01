mayor=None
menor=None

n = int(input('Ingrese cantidad  de numeros para saber el mayor y el menor ---> ' ))

for i in range (n):
    numero = int(input('Ingrese los numeros --->'))

    if mayor is None and menor is None:
       mayor=numero
       menor=numero


    if(numero > mayor):
        mayor = numero
    elif(numero < menor):
        menor = numero

print('El numero mayor es --->',mayor)
print('El numero menor es --->',menor)

        
        

