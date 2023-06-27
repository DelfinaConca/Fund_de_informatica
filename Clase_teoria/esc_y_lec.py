#!/bin/python3

with open("mi_nombre.txt", "a") as mi_archivo:
    mi_archivo.write("Delfina Conca")

# crear archivo con los primeros 5 caracteres
texto_leido = open("archivo.txt","r").read()

texto_para_escribir = texto_leido [0:6]
with open ("nuevo_archivo.txt","a") as mi_arch:
   mi_arch.write(texto_para_escribir)

arch = open("hola.txt", "r")
print(arch)
print(arch.read())