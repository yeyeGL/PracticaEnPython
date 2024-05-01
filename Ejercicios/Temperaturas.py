temperaturas = []
tMayores = 0

n_temperatura = int(input('Ingrese la cantidad  de temparaturas --> '))

for i in range(n_temperatura):
    temperaturaI = int(input('Ingrese las temperaturas de la city --> '))
    temperaturas.append(temperaturaI)


promedio = sum(temperaturas) / len(temperaturas)

for temperaturaI in temperaturas:
    if temperaturaI > promedio:
     tMayores +=1
    
    
print('El promedio de las temperaturas es de -->',promedio)
print('El numero de temperaturas mayores al promedio son -->',tMayores)



