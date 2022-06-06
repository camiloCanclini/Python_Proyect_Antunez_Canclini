import random, json
from turtle import width
def purchaseResume(movieName, ticketNumber, price, mailAccount):
    widthLine = "{:^60}" # esto es para que...print("{:^50}".format("...")
    print(widthLine.format("_______Resumen de la Compra_______"))
    print(widthLine.format("Pelicula: "+movieName)) 
    print(widthLine.format("------------------------"))
    print(widthLine.format("Cantida de tickets: "+str(ticketNumber))) 
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
def billboardMovies():
    jsonFile = open("peliculasCartelera.json")
    peliculas = json.load(jsonFile)
    for i in peliculas:
        print(i["titulo"])
        print(i["horarios"])
    jsonFile.close()
     
ticketPrint("Batman","A4", "13 de junio", "17:30")
purchaseResume("batman",5,2500,"cuenta@gmail.com")
#billboardMovies()
