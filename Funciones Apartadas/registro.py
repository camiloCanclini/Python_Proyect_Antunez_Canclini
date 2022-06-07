#Register
"""
registro = {}

terminar = True
while terminar == True:
    print ("Obtenga su entrada de cine sin salir de su casa!")
    print("Si usted ya es cliente simplemente ingrese su usuario y contraseña.")
    print ("Por favor, seleccione la opcion correspondiente: ")
    print ("1) Registrarse")
    print ("2)Ingresar")
    opcion = int(input("Ingrese una opcion:"))

    if opcion == 1:
        nombre = input ("Nombre: ")
        apellido = input ("Apellido: ")
        mail = input ("mail: ")
        if registro.get(mail) == None:
            registro = {"E-mail": mail}
        elif registro.get(mail) == mail:
            print ("El usuario ya existe, intente nuevamente")
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
        print (registro)
        print("Desea ingresar a su cuenta? Ingrese 'y' para 'SI', N para 'NO'")
        opcion2 = input ("Elija una opcion:")

        if opcion2 == 'y':
            print("aca iria la funcion de ingreso")
        elif opcion2 == 'n':
            break
    if opcion == 2 or opcion2 == 'y':
        print (registro)
        if registro == {}:
            print ("debes registrarte primero")
        else:
            verificar = True
            while verificar == True:
                usuario = input ("Usuario: ")
                contraseña_ingreso = input ("Contraseña: ")
                for i in registro.values():
                    if usuario in registro.values() and contraseña_ingreso in registro.values():
                        print ("Ingresaste")
                        verificar = False
                        terminar = False
                        break
                        
                    elif usuario not in registro.values() or contraseña_ingreso not in registro.values():
                        print ("Usuario y/o contraseña no validos")  
                        break       
                 
                
"""

#Register

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



def login():
    verificar = True
    while verificar == True:
        usuario = input ("Usuario: ")
        contraseña_ingreso = input ("Contraseña: ")
        for i in registro.values():
            if usuario in registro.values() and contraseña_ingreso in registro.values():
                print ("Ingresaste")
                verificar = False
                break
                    
            elif usuario not in registro.values() or contraseña_ingreso not in registro.values():
                print ("Usuario y/o contraseña no validos")  
                break



terminar = True
while terminar == True:
    print ("Obtenga su entrada de cine sin salir de su casa!")
    print("Si usted ya es cliente simplemente ingrese su usuario y contraseña.")
    print ("Por favor, seleccione la opcion correspondiente: ")
    print ("1) Registrarse")
    print ("2)Ingresar")
    opcion = int(input("Ingrese una opcion:"))

   
    if opcion == 1:
        registerAccount()
        print (registro)
    if opcion == 2:
        if registro == {}:
            print ("No hay")
        else:
            login()
            break

        




                 




