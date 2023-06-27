#!/usr/bin/env python3
import os, glob, sys

#EJERCICIO 1

def start_with(letra,archivo):
    count = 0
    with open("hola.txt","r") as archivo:
        for line in archivo:
            if (line[0] != letra.lower() and line[0]!= letra.upper()):
                count +=1
    print("El numero de lineas que no empiezan con", letra , "es", count)
start_with("P","hola.txt")

#EJERCICIO 2
def lee_n_lineas(n,archivo):
    with open("hola.txt","r") as archivo:
        for i in range(n):            #rango() tiene 3 parametros (inicio,hasta,como contar)
            print(archivo.readline())
lee_n_lineas(3,"hola.txt")


#EJERCICIO 3
def ultimas_lineas(n,archivo):
    texto = open("hola.txt","r").readlines() #esta guarando en una lista el contenido del archivo
    for i in range((len(texto)-n),(len(texto))):   #esta imprimiendo las n ultimas
        print(texto[i])
ultimas_lineas(2,"hola.txt")

#EJERCICIO 4
def cant_palabras(archivo):
    with open("hola.txt","r")as archivo:
        contenido = archivo.read()
        palabras = contenido.split()
        num_palabras = len(palabras)
    print ("Cantidad de palabras que hay:",num_palabras)
cant_palabras("hola.txt")

#EJERCICIO 5
def reemplazar(letra,archivo_leer,archivo_salida):
    with open(archivo_salida,"a") as archivo:
        with open(archivo_leer,"r") as archivo1:
            texto = archivo1.read()
            texto = texto.replace(letra,letra + "\n")
            archivo.write(texto)     
reemplazar("c","hola.txt","hola2.txt")

#EJERCICIO 6
def eliminar_saltos_linea(archivo_leer,archivo_salida):
    with open(archivo_salida,"a") as archivo:
        with open(archivo_leer,"r") as archivo1:
            texto = archivo1.read()
            texto = texto.replace("\n", "")
            archivo.write(texto)

eliminar_saltos_linea("hola.txt","hola3.txt")          

#EJERCICIO7
# def identificar_palabra_larga(archivo_entrada):
#     max_long = 0
#     palabra = ""
#     with open (archivo_entrada,"r") as archivo:
#         lista_palabras = archivo.read().split()
#         for palabra in lista_palabras:
#             if len(palabra) > max_long:
#                 max_long = len(palabra)

# print("La palabra mas larga es",palabra,"con",max_long,"caracteres") 
# identificar_palabra_larga("hola.txt")

#EJERCICIO 7
# def palabra_larga(archvio):
#     max_ling = 0
#     palabra = ""
#     with open (archivo ,"r") as f:
#         lista_palabras = f.read().split()
#         for palabra in lista_palabras:
#             if len(palabra) > max_long:
#                 max_long = len(palabra)

# print("La palabra mas larga es", palabra  , "con", max_long, "caracteres")
# identificar_palabra_larga("hola.txt")

# #EJERCICIO 8
def juntar_archivos(archivo1,archivo2,archivo3):
    with open(archivo1,"r") as a1, open(archivo2,"r") as a2, open(archivo3,"a") as a3:
        a3.write(a1.read() + a2.read())
juntar_archivos("documento","documento2","documento3")



# COMO CREAR ARCHIVOS
# nombre_archivo = "nuevo.txt"

# with open(nombre_archivo,"w") as archivo:
#     archivo.write("Reemplazar el contenido anterior\n")
#     archivo.write("Segunda prueba\n")  # se escribe en la misma linea, por eso hay que poener \n 


# # COMO AGREGAR DATOS A UN ARCHIVO 
# nombre_archivo = "nuevo.txt"

# with open(nombre_archivo,"a") as archivo:
#     archivo.write("Pruba de append \n")
#     archivo.write("Segunda prueba de append\n")



# EJ PRACTICA PARCIAL
#Definir un procedimiento que lea los archivos .txt que estan en la carpeta marzo, y copie la primera linea de cada uno en un archivo dentro de la carpeta resultados(qeu debe estar adentro de new)
# la carpeta new seria la el repositorio que nos bajamos del parcial
# la carpeta datos tiene la carpeta marzo y esta tiene varios archivos que hya que leer la primera linea de eso

#PASO A PASO:
#1. nos movemos a la carpeta marzo
#2. extraemos los .txt
#3. leemos la primera linea --> recorrer todos los archivos y de cada uno leemos la primera linea
#4. hacer carpeta de salida = resultados
#5. hacer archivo (salida.txt) dentro de resultados 
#6. poner lineas en archivo nuevo

def primeras_lineas(path_a_txt,path_resultado,salida): 
    os.chdir(path_a_txt)                    # os.chdir para movernos al archiv, Tiene dos parametro= entrada
    textos = glob.glob("*.txt")
    primera_linea = []     #armamos una lista vacia para despues guardar la primera linea de cada archivo
                           # como funciona len  = print(len(primera_linea)) nos dice cuantas cosas hay en esa lista

    for txt in textos:                      #para cada archivo abrimos uno por uno
        with open(txt,"r") as texto:
            primera_linea.append(texto.readline())   # en la lista que creamos le decimos que agregue la primera linea

    os.chdir("../..")                     #hacemos dos veces .. porque tenemos que salir de marzo y de datos
    os.mkdir(path_resultado)              #creamos la carpeta resultados
    os.chdir(path_resultado)

    with open(salida,"a") as final_txt:   #conviene abrirlo como a porque si es w no lo podemos reutilizar
        for linea in primera_linea:       # linea es cada elemento de la lista primera_linea (donde estan las primerar lineas de cada archivo)
            final_txt.write(linea)        # solamente se puede escribir strings entonces tenemos que recorrer linea por linea en la lista


primeras_lineas("datos/marzo","resultado","salida.txt")


