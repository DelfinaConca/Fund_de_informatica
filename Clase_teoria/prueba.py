import requests

respuesta = requests.get("https://api.github.com/users/ajvelezrueda/orgs")
datos = respuesta.json()
#1.en cuantas org esta involucrado el usuario
print(len(datos[1])) 

#2.lista de los nombres de las orgs en la que esta involucrado
print(respuesta)
print(respuesta.headers)

respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
contenido_respuesta = respuesta.json()

#las cosas que tienen guardada: nso da por respuesta todos los contenidos asociados al recurso ditto con los detalles de abilities, base_experiene, game_indicies,height.....
print (contenido_respuesta.keys) 

#content type:json
print(respuesta.headers["Content-Type"])

#status code:
print(respuesta.status_code)

#cuantas habilidades tiene
print(len(contenido_respuesta["abilities"])) # me da las habilidades + len para saber la CANTIDAD de habilidades
                                            # si no pongo el len me devuelve las habilidades nomas

#1 describir las partes de la url
#https: protocolo
#pokeapi.co : dominio
#/api/v2... : recursos
