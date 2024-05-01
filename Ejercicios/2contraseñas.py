contraseña1 = input('Ingrese la contraseña --> ')
contraseña2 = input('Ingrese la contraseñ de validacion --> ')

while contraseña1 != contraseña2:
    print('La contaseña esta incorrecta intente de nuevo')
    print('=====================================')
    contraseña1= input('Ingrese la contraseña 1 --> ')
    contraseña2 = input('valide la contraseña 2 --> ')

print('La contraseña confirmada es --> ',contraseña1)

