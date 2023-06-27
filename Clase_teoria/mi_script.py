print ("Corriendo el script")
#comentario 
import os, sys 

usuario = sys.argv[1]

def saludador(nombre):
    return "Hola " + nombre

if __name__ == "__main__":
   print (saludador(usuario))


