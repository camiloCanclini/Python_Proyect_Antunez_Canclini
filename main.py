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
def movieSearch(search):
    #Aca iria el codigo de la API, agrego algo para que la funcion no me tire error
    search = "batman"
    return search
def seatSearch():
     ("Aqui esta la matriz")
    #Hay que hacer una matriz o arreglo que contenga los lugares ocupados y disponibles
    #Deberiamos permitir que seleccionen solo los lugares disponibles
    #Para selecionarlos podemos hacer como si fuera un batalla naval con letras y numeros de posicion
def purchaseResume():
    print ("Informacion del ticket")
    #Tenemos que armar un resumen de lo que se pidio
def ticketPrint(movieName, seatPlace):
    #Aca deberia salir cada ticket comprado, o sea por persona
    #Necesitamos el lugar y nombre de la peli
    #Deberiamos añadir un generador de codigo, para que no se pueda falcificar
    print("Aqui esta el ticket final")
while True:
    print ("---Bienvenido al Sistema de Cine---")
    print ("-Elija una opción a continuación---")
    print ("1) Buscar pelicula")
    print ("2) Registrarse como cliente")
    print ("3) Salir")
    optionSelected = int(input("-> "))
    if optionSelected==1:
        movieName = input("Ingrese el nombre de la pelicula \n-> ")
        #movieYear = input("Ingrese el año de la pelicula \n-> ")
        movieSelected, error = movieSearch(movieName)
        if movieSearch(error) == 1:
            print ("La pelicula no fue encontrada")
            continue #vuelve a las opciones
        numberTickets = int(input("Ingrese cantidad de tickets \n-> "))
        if (numberTickets>10):
            print ("Usted a requisado demasiados tickets (Maximo 10) ")
            continue #vuelve a las opciones
        print ("A continuacion se le presentara matriz con los lugares disponibles")
        seatSearch()
        placeSelected = int(input("Ingrese los lugares \n-> "))
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
    if optionSelected == 2:
        print ("hola")
        continue
    if optionSelected ==3:
        print ("Finalizacion del programa")
        break

