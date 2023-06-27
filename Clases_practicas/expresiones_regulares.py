#!/usr/bin/env python3
import re 

# #EJERICIO 1
def caracteres_permitidos(string):
    return bool(re.search('[a-z A-Z 0-9.]'), string)
#o
#EJERCICIO1
string1 = "hola como estas"
def carac_permitido(string):
    patron = "[a-z A-Z 0-9]+"
    return bool(re.search(patron,string))
print(carac_permitido(string1))


#EJERCICIO 2
string2 = "hola como estas"
def todos_carac_permitidos(string2):
    patron = "[^a-z A-Z 0-9.]"
    return not bool(re.search(patron,string2))
print(todos_carac_permitidos)
# o 
#EJERCICIO 2
def todos_caract_permitidos(string):
    return not bool (re.search('[^a-z A-Z 0-9.]'),string)

#EJERCICIO 3 - a
string3 = "a,h,he,heeee"
def contar_patron(string3):
    patron="he*"                             #el * dice que este 0 o mas veces: solo a la e. El * solo toma el caracter a su izq
    if re.search(patron,string3) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
print(contar_patron(string3))

#EJERCICIO 3 - b
def  contar_patron(string3):
    patron="he+"                             
    if re.search(patron,string3) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
print(contar_patron(string3))

#EJERCICIO 3 - c
def  contar_patron(string3):
    patron="he?"                             
    if re.search(patron,string3) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
print(contar_patron(string3))
    
#EJERCICIO 3 - d
def  contar_patron(string3):
    patron="he{2,3}"                             
    if re.search(patron,string3) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
print(contar_patron(string3))

#EJERCICIO 4
def palabras_unidas(string):
    patron="^[a-z]+_[a-z]+$"
    if re.search(patron,string) is not None:
        return "Patron encontrado"
    else:
        return "Patron no encontrado"

#o
#Ejercicio 4:
string4= "hola_comoestas"
def unidas(string4):
    patron= "^[\w]+_[\w]+$"
    if re.search(patron,string4) is not None:
        return "Patron encontrado"
    else:
        return "Patron no encontrado"
print(unidas(string4))    
 
#EJERCICIO 8 
string8 = "Hoy movimos 10 cajas de lugar,en 3 edificios distintos para llevar a 12 casas"
def palabras_unidas(string8):
    patron="\D+"                           # no numerico
    resultado = re.split("\D+",string8)     #cada vez que haya un numero lo parte (split)
    for elemento in resultado:
        print(elemento)
palabras_unidas(string8)

# #EJERCICIO 9
string9 = "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"
def caract_entre_guiones(string9):
    patron = r"-(.*?)-"                    # . cualquier cosa    * 0 o 1 o mas veces    ? fijar matches internos  - - entre guiones
    return re.findall(patron,string9)       

print(caract_entre_guiones(string9))

# o
#Ej 9:
def caract(string9):
    patron= "-(.*?)-"
    return re.findall(patron,string9)
print(caract(string9))

#EJERCICIO 10
string10= "hola @ como estas & bien"
def get_substr(string):
    patron = "[@|&] (.*?) [@|&]"
    return re.findall(patron,string10)



print(get_substr(string10))

# #EJERCICIO 11
lista = ["Práctica Python", "Práctica C++", "Práctica Fortran"]
def dos_P(lista):
    patron = "(P\w*)\W(P\w*)"             # P\w* --> empiece con P siga con letras  \W no alfanumerio porque tiene que haber un espacio podemos poner \s
    for elemento in lista:
        resultado = re.match(patron,elemento)
        if resultado is not None:
            print(resultado.group())            # la parte que coincide con lo que le digo

dos_P(lista)

# EJERCICIO 5
string5 = "3,4,5,6,7,8" 
def empieza_con(string5):
    patron = "^3"
    if(re.search(patron,string5)) is not None:
        return "string empieza con el numero especifico"
    else:
        "string no empieza con el numero especifico"
print(empieza_con(string5))
 
#EJERCICIO 6
lista6 = ["hola como estas","bien y vos","bien bien"]
def se_encuentra(lista6):
    patron = "[bien bien]"
    for elemento in lista6:
        return bool(re.search(patron,elemento))
    
print(se_encuentra(lista))

#EJERCICIO 7
string7 = "Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números."
def letras(string):
    patron = "[a-z A-Z \d \s]+"
    if re.search(patron,string7):
        return "se encuentran minusculas, mayusculas, espacios y numeros"
    else:
        return "no se encuentra nada"
print(letras(string7))

#EJERCICIO 12
string12 = "hola_como estas:hola_como estas:"
def reemplazar(string12):
    patron = "[\s _  :]"
    return re.sub(patron,"|",string12)
print (reemplazar(string12))

#EJERCICIO 13
string13 = ",hola como .estas?"
def reemplazar(string13):
    patron = "[\W +]"
    return re.sub(patron,"_",string13)
print (reemplazar(string13))

# #EJERCICIO 14
string14 = "hola como estas"
def reemplazar_espacioas_tabulaciones(string14):
    patron = "[\s \t]"
    return re.sub(patron,";",string14)
print(reemplazar_espacioas_tabulaciones(string14))

#EJERCICIO 15
mail = "delfi_._-conca@hotmail.com" 
def mail_correcto(mail):
    patron = "^\w+[-._]?\w*@[a-z]+[-._]?\.[a-z]+$"       #^\w empiece con alfanumerico [.-_]? que puede tener uno de esos caracteres \w* puede volver a tener un alfanumerico 0 o mas veces, despues del @ [a-z]+ solo puede haber letras al menos 1, [.-_]? puede vovler a aparecer, \.[a-z]$ si o si tiene que haber un .(se opne con \. para especificar que es un. literal) y terminar con letras al menos una de a-z (seria el com)  
                                                        # no puede ser el . porque las & y "" no pueden estar en el mail
    if re.search(patron,mail):
        return "esta escrito correctamente"
    else:
        return "no esta escrito correctamente"
    
print(mail_correcto(mail))

#EJ PRACTICA
texto = "+541190375826"
def encontrar(texto):
    patron = "\+5411([\d]{8})"
    return bool (re.search(patron,texto))

print (encontrar(texto))

