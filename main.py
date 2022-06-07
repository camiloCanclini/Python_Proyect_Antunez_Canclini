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
#Definicion de Librerias, funciones y metodos----------------------------------------------------------    
import json, random

def billboardMovies():
    jsonFile = open("peliculasCartelera.json")
    data = json.load(jsonFile) # Se hace la conversion de la respuesta a Json
    #print(type(data))
    jsonFile.close()
    return data
def calcPrice(numberTickets):
    IVA = 1,21
    priceTicket = 300
    return (priceTicket*numberTickets)*IVA
def seatSearch():
     ("Aqui esta la matriz")
    #Hay que hacer una matriz o arreglo que contenga los lugares ocupados y disponibles
    #Deberiamos permitir que seleccionen solo los lugares disponibles
    #Para selecionarlos podemos hacer como si fuera un batalla naval con letras y numeros de posicion
def templateJsonFile():# Esta funcion limpia el JSON y crea el usuario admin
    templateJsonUsers = {
        0:{
            "name": "administratorAccount",
            "email": "admin",
            "password": "admin"}
        } 
    jsonString = json.dumps(templateJsonUsers)
    jsonFile = open("cuentas.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
def purchaseResume(movieName, numberTickets, price, mailAccount):
    widthLine = "{:^60}" # esto es para que...print("{:^50}".format("...")
    print(widthLine.format("_______Resumen de la Compra_______"))
    print(widthLine.format("Pelicula: "+movieName)) 
    print(widthLine.format("------------------------"))
    print(widthLine.format("Cantida de tickets: "+str(numberTickets))) 
    print(widthLine.format("------------------------"))
    print(widthLine.format("Precio Total (IVA incluido): $"+str(price))) 
    print(widthLine.format("------------------------"))
    print(widthLine.format("Mail de la cuenta: "+mailAccount))
    print(widthLine.format("_________________________________"))
def ticketPrint(movieName, seatPlace, movieDate, movieSchedule):
    ticketCode = "CODE"
    widthLine = "{:^60}" # esto es para que...print("{:^50}".format("...")
    for i in range(0,10):
        ticketCode += str(random.randint(0,9))
    print(widthLine.format("_____________Ticket_____________"))
    print(widthLine.format("CODIGO DE TICKET: "+ticketCode)) 
    print(widthLine.format("------------------------"))
    print(widthLine.format("Pelicula: "+movieName)) 
    print(widthLine.format("------------------------"))
    print(widthLine.format("Asiento: "+seatPlace)) 
    print(widthLine.format("------------------------"))
    print(widthLine.format("Fecha: "+movieDate)) 
    print(widthLine.format("------------------------"))
    print(widthLine.format("Horario: "+movieSchedule)) 
    print(widthLine.format("_________________________________"))  
def login(usersData):
    while True:
        emailSession = None
        usuario = input ("\nEmail: ")
        contraseña_ingreso = input ("Contraseña: ")
        for i in usersData.values():
            #print(i)
            if usuario == i["email"] and contraseña_ingreso == i["password"]:
                emailSession = i["email"]
                break       
        if emailSession == None:
            print ("\nUsuario y/o contraseña no validos")
        else:
            break
    return emailSession
def registerAccount():
    name = input ("Nombre Y Apellido: ")
    email = input ("Email: ")
    while True:
        dni = (input ("DNI: "))
        if len(dni) > 10:
            print ("Demasiados caracteres")
        else:
            break
    #Verificacion de contraseña
    repeticion = 3
    while repeticion > 0:
        password = input ("Ingrese una contraseña: ")
        if len(password) < 8:
            print ("Debe ingresar minimo 8 caracteres")
            continue
        else:
            flag = input ("ingrese nuevamente la contraseña: ")

            if password == flag:
                break
            elif repeticion == 0:
                print ("Se acabaron los intentos")
                break
            else: 
                print ("ERROR. Las contraseñas no coinciden")
                repeticion -= 1
                print ("Le quedan", repeticion, "intentos")
    idAccount=""
    while True:
        for i in range(0,4):
            idAccount += str(random.randint(1,9))
            #print(idAccount)
        jsonFile = open('cuentas.json')
        usersRegistered = json.load(jsonFile)
        if usersRegistered.get(idAccount) == None:
            usersRegistered [idAccount] = {
                "name": name,
                "email": email,
                "password": password,
                "dni": dni
                }
            #print (usersRegistered)
            jsonString = json.dumps(usersRegistered)
            jsonFile = open("cuentas.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close()
            #print (usersRegistered)
            break
        else:
            print ("el id ya existe")
def getUsers():
    jsonFile = open("cuentas.json")
    data = json.load(jsonFile)
    return data
#print(getUsers())
#Comienzo del Programa---------------------------------------------------------------------------------          
while True:
    print ("\nObtenga su entrada de cine sin salir de su casa!")
    print("Si usted ya es cliente simplemente ingrese su usuario y contraseña.")
    print ("Por favor, seleccione la opcion correspondiente:\n")
    print ("1) Registrarse")
    print ("2)Ingresar")
    try:# Si esto tira error se realiza el except, esto se hace por si no se ingresa un numero 
        optionSelected = int(input("Ingrese una opcion:"))
    except:
        print("Elija de nuevo porfavor...")
        continue
    if optionSelected == 1:
        registerAccount()
    elif optionSelected == 2:
        emailSession = login(getUsers())
        while True:
            print ("\n---Bienvenido al Sistema de Cine---")
            print ("---Email de la sesion:",emailSession,"---")
            print ("-Elija una opción a continuación---")
            print ("1) Ver peliculas en cartelera")
            print ("2) Salir")
            try:
                option2Selected = int(input("-> ")) 
            except:
                print("Elija de nuevo porfavor...")
                continue
            if option2Selected==1:
                movies = billboardMovies()
                print("\nPeliculas en Cartelera:\n")
                for i in movies.values():
                    print (i["titulo"])
                numberTickets = int(input("\nIngrese cantidad de tickets \n-> "))
                if (numberTickets>10):
                    print ("Usted a requisado demasiados tickets (Maximo 10) ")
                    continue #vuelve a las opciones
                price = calcPrice(numberTickets)
                
                print ("A continuacion se le presentara matriz con los lugares disponibles")
                seatSearch()
                print ("Esta informacion es correcta")
                purchaseResume(movieName, numberTickets, price, emailSession)
                confirmation = input("Ingrese Y para confirmar, N para cancelar")
                if confirmation == "N":
                    continue
                else:
                    ticketPrint()
                    print ("Muchas gracias por confiar en nosotros")
                    input("Presione ENTER para continuar...")
                    print ("Volviendo al menu")
                    continue
            if option2Selected ==2:
                print ("Volviendo Al Menu Principal...")
                break
                
    
