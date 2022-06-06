registro = {}
def registerAccount():
    global registro
    nombre = input ("Nombre: ")
    apellido = input ("Apellido: ")
    mail = input ("mail: ")
    while True:
        dni = (input ("DNI: "))
        if len(dni) > 10:
            print ("Demasiados caracteres")
        else:
            break

    repeticion = 3
    while repeticion > 0:
        contraseña = input ("Ingrese una contraseña: ")
        if len(contraseña) < 8:
            print ("Debe ingresar minimo 8 caracteres")
            continue
        else:
            verificacion = input ("ingrese nuevamente la contraseña: ")

            if contraseña == verificacion:
                break
            elif repeticion == 0:
                print ("Se acabaron los intentos")
                break
            else: 
                print ("ERROR. Las contraseñas no coinciden")
                repeticion -= 1
                print ("Le quedan", repeticion, "intentos")

    registro = {"Nombre": nombre, "Apellido": apellido, "DNI":dni, "E-mail": mail, "Contraseña" : contraseña}

