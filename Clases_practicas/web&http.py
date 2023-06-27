import requests

# EJERCICIO 1
# a) El dominio es: pokeapi.co
# b) 
respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
pikachu = respuesta.json()
print("el status code es" , respuesta.status_code)

print("el content type es", respuesta.headers["Content-Type"])

print(pikachu["forms"])

#c) 
respuesta1 = requests.get("https://pokeapi.co/api/v2/pokemon")
contenido_respuesta1 = respuesta1.json()

print("tiene",contenido_respuesta1["count"],"pokemones")

#d) 
# ("https://pokeapi.co/api/v2/pokemon/abilities")
# ("https://pokeapi.co/api/v2/pokemon/abilities/2")

#f) 
respuesta3 = requests.get("https://pokeapi.co/api/v2/pokemon/sylveon")
sylveon = respuesta3.json()

#opcion optima:
# with open("ficha_tecnica_pokemon.txt","wb") as ficha:
#     ficha.write(respuesta.content)
#     ficha.write(b'\n')
#     ficha.write (respuesta3.content)
    
#otra opcion:
# str(respuesta.json())



#EJERCICIO 2
respuesta2 = requests.get("https://jsonplaceholder.typicode.com/todos")
contenido_respuesta2 = respuesta2.json()

# a) El dominio es: jsonplaceholder.typicode.com
# b) 
print("el status code es",respuesta2.status_code)

print("el content type es", respuesta2.headers["Content-Type"])

# c) post --> para agregar contenido a la api. Hay que definir un diccionario y el header
data = {"userId":11,"id":2,"title":"quis ut nam facilis et officia qui", "completed": True}

headers = {"Content-Type": "application/json; charset=utf-8"}

# a= requests.post("https://jsonplaceholder.typicode.com/todos",data = json.dumps(data),headers=headers)
# a.json()
