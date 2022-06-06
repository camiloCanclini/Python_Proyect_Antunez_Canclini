"""
__________________________________________________________________________________
Sistema Cine (Agenda que guarde peliculas en cartelera)
con ticket (Compra candybar y entrada)- [en caso de que quede corto, le 
ponemos una segunda agenda que guarde la info del cliente]
__________________________________________________________________________________
apikey=71066fc3
omdbapi.com <-- esta es la pagina de la API, desde aca podemos probar comandos
En este caso pasamos por la URL el parametro "s", este es el nombre de la pelicula
Para que la URL funcione necesitamos pasar este paremetro
__________________________________________________________________________________
Developers: Agustin Antunez - Canclini Camilo
__________________________________________________________________________________



"""
import json, random
from urllib.request import urlopen

def movieSearch():
    url = 'http://www.omdbapi.com/?apikey=71066fc3&s='
    movieName = input("Ingrese el nombre de la pelicula \n-> ")
    #movieYear = input("Ingrese el año de la pelicula \n-> ")
    url += movieName # Se suma el nombre de la pelicula a la URL de la API
    response = urlopen(url) # Se hace la petición a la API y se guarda la respuesta en una variable
    data = json.loads(response.read()) # Se hace la conversion de la respuesta a Json
    #print(data)
    j=1
    for i in data["Search"]:
        print(j,")",i["Title"])
        j += 1
def seatSearch():
     ("Aqui esta la matriz")
    #Hay que hacer una matriz o arreglo que contenga los lugares ocupados y disponibles
    #Deberiamos permitir que seleccionen solo los lugares disponibles
    #Para selecionarlos podemos hacer como si fuera un batalla naval con letras y numeros de posicion
def purchaseResume():
    print("")
def ticketPrint(movieName, seatPlace):
    #Aca deberia salir cada ticket comprado, o sea por persona
    #Necesitamos el lugar y nombre de la peli
    #Deberiamos añadir un generador de codigo, para que no se pueda falcificar
    print("Aqui esta el ticket final")
def templateJsonFile():# Esta funcion limpia el JSON y crea el usuario admin
    templateJsonUsers = {
        0:{
            "mail": "admin",
            "password": "admin"}
        } 
    jsonString = json.dumps(templateJsonUsers)
    jsonFile = open("cuentas.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
def registerAccount(email, password):
    idAccount="1"
    while True:
        for i in range(0,4):
            idAccount += str(random.randint(1,9))
            #print(idAccount)
        jsonFile = open('cuentas.json')
        usersRegistered = json.load(jsonFile)
        if usersRegistered.get(idAccount) == None:
            usersRegistered [idAccount] = {
                "mail": email,
                "password": password
                }
            #print (usersRegistered)
            jsonString = json.dumps(usersRegistered)
            jsonFile = open("cuentas.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close()
            print (usersRegistered)
            break
        else:
            print ("el id ya existe")     


#Registro
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
            while True:
                print ("---Bienvenido al Sistema de Cine---")
                print ("-Elija una opción a continuación---")
                print ("1) Buscar pelicula")
                print ("2) Registrarse como cliente")
                print ("3) Salir")
                optionSelected = int(input("-> "))
                if optionSelected==1:
                    movieSearch()
                    #if movieSearch(error) == 1:
                        #print ("La pelicula no fue encontrada")
                        #continue #vuelve a las opciones
                    numberTickets = int(input("Ingrese cantidad de tickets \n-> "))
                    if (numberTickets>10):
                        print ("Usted a requisado demasiados tickets (Maximo 10) ")
                        continue #vuelve a las opciones
                    print ("A continuacion se le presentara matriz con los lugares disponibles")
                    seatSearch()
                    print ("Esta informacion es correcta")
                    purchaseResume()
                    confirmation = input("Ingrese Y para confirmar, N para cancelar")
                    if confirmation == "N":
                        continue
                    else:
                        ticketPrint()
                        print ("Muchas gracias por confiar en nosotros")
                        print ("Volviendo al menu")
                        a=input("")
                        continue
                if optionSelected ==3:
                    print ("Finalizacion del programa")
                    break

