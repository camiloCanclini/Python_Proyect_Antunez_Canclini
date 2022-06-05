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

