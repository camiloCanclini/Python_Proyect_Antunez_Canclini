#Esta funcion es para buscar la pelicula con la API OMDBAPI#
from urllib.request import urlopen
import json
def movieSearchByApi(movieName):
    url = 'http://www.omdbapi.com/?apikey=71066fc3&s='
    #movieYear = input("Ingrese el año de la pelicula \n-> ")
    url += movieName # Se suma el nombre de la pelicula a la URL de la API
    response = urlopen(url) # Se hace la petición a la API y se guarda la respuesta en una variable
    data = json.loads(response.read()) # Se hace la conversion de la respuesta a Json
    print(data)
    j=1
    for i in data["Search"]:
        print(j,")",i["Title"])
        j += 1
#Las siguientes lineas son para hacer un ejemplo
movieName=input("Ingrese el nombre de la pelicula --> ")
movieSearchByApi(movieName)