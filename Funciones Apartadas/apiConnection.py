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
from urllib.request import urlopen
import json

url = 'http://www.omdbapi.com/?apikey=71066fc3&s='

movieName = input("Ingrese el nombre de la pelicula a buscar")
url += movieName
response = urlopen(url)
data = json.loads(response.read())
print(data)
for i in data["Search"]:
    print(i["Title"])
