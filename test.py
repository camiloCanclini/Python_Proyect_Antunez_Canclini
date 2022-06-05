import random
def purchaseResume(movieName, ticketNumber, price):
    cstr="RESUMEN"
    print(cstr.center(25, '_'))
    cstr=""
    print(cstr.center(25, '/'))
    cstr="Pelicula: "+movieName
    print(cstr.ljust(25, ' '))
    cstr=""
    print(cstr.ljust(25, '/'))
    cstr="Cantidad de Tickets: "+ str(ticketNumber)
    print(cstr.ljust(25, ' '))
    cstr=""
    print(cstr.ljust(25, '/'))
    cstr="Precio Total\ncon IVA INCLUIDO: "+ str(price)
    print(cstr.ljust(25, ' '))
    cstr=""
    print(cstr.ljust(25, '/'))
    cstr="Cuenta: + cuenta"
    print(cstr.ljust(25, ' '))
    cstr=""
    print(cstr.ljust(25, '/'))
    cstr="Password: + password"
    print(cstr.ljust(25, ' '))
    cstr=""
    print(cstr.center(25, '-')) 
purchaseResume("batman",5,2500)
def ticketPrint(movieName, seatPlace):
    ticketCode = "CODE"
    for i in range(0,10):
        ticketCode += str(random.randint(0,9))
    cstr="TICKET"
    print(cstr.center(25, '_'))
    cstr="CODIGO DE TICKET: \n"+ticketCode
    print(cstr.ljust(25, ' '))
    cstr=""
    print(cstr.center(25, '/'))
    cstr="Pelicula: "+movieName
    print(cstr.ljust(25, ' '))
    cstr=""
    print(cstr.ljust(25, '/'))
    cstr="Asiento: "+ str(seatPlace)
    print(cstr.ljust(25, ' '))
    cstr=""
    print(cstr.center(25, '-')) 
ticketPrint("Batman","A4")
    