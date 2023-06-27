# def eneavo(numero):
#     try:
#         print(1/numero)
#     except ZeroDivisionError:
#         print("No se puede dividir por",numero)

#     except TypeError:
#         print("El",numero, "es un string")

#     print(numero)

# eneavo("9")
# eneavo(0)

#EJERCICIO 1
# lista_super = ["tomate", "fideos", "arvejas", "detergente", "jabón", "alcohol"]
# def super(lista_super):
#     try:
#         lista_super + "arroz"
#     except TypeError:
#         print("no se le pueden agregar string a la lista")

# super(lista_super)

#EJERCICIO 2
# def lista(lista_n,n):
#     lista_nueva =[]
#     try:
#         for numero in lista_n:
#             lista_nueva.append(numero/n)
#         return(lista_nueva)
#     except TypeError:
#         return("hay un string")

# print(lista([2,4,6,8],2))
# print(lista([2,4,6,"8"],2))
# print(lista([2,4,6,8],"2"))

#EJERCICIO 3
def lista_positivos(lista_de_num,b):
    lista_p = []
    for i in lista_de_num:
        if i < 0:
            raise Exception (str(i) + "no es positivo")
        if i > 0:
            lista_p.append(i)
    
    return lista_p

print(lista_positivos([1,2,3]))
print(lista_positivos([1,2,-1]))

