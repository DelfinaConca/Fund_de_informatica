#EJERCICIO 1
#INTERFAZ = energia, comer, acariciar, estaDebil
#ESTADO = self._alimento, self._caricias

#EJERCICIO 3
class Notebook:
    def __init__(self,marca,modelo,precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def aplica_descuento(self,numero):
        self.precio = self.precio - (self.precio * (numero /100))
        return self.precio
    
MIMI = Notebook("Dell","AG 1.2",500)
print(MIMI.marca)
print(MIMI.precio)
print(MIMI.modelo)
print(MIMI.aplica_descuento(25))


#EJERCICIO 4
class Contador:
    def __init__(self,contador,comando):
        self.contador = contador
        self.comando = comando
        
    def inc(self):
        self.contador = self.contador + 1 
        self.comando = "incremento"

    def dis(self):
        self.contador = self.contador - 1
        self.comando = "disminución"
        

    def reset(self):
        self.contador = 0 
        self.comando= "reset"

    def valorActual(self):
        return self.contador 
        
    def valorNuevo(self,nuevoValor):
        self.contador = nuevoValor
        self.comando = "actualización"
        

# EJERCICIO 5
    def ultimoComando(self):
       return self.comando

contador = Contador(10, "")

contador.inc()
contador.inc()
contador.dis()
contador.inc()
print(contador.valorActual())
contador.valorNuevo(27)
contador.dis()
contador.dis()
print(contador.valorActual())
print(contador.ultimoComando())


# EJERCICIO 6
class Calculadora:
    def __init__(self):
        self.rtado = 0

    def cargar(self,numero):
        return numero

    def sumar(self,numero):
        self.rtado = self.rtado + numero

    def restar(self,numero):
        self.rtado = self.rtado - numero

    def multiplicar(self,numero):
        self.rtado = self.rtado * numero

    def valorActual(self):
        return self.rtado

calculadora = Calculadora()

calculadora.cargar(0)
calculadora.sumar(4)
calculadora.multiplicar(5)
calculadora.restar(8)
calculadora.multiplicar(2)
print(calculadora.valorActual())    

#EJERCICIO 7
class Gorriones:
    def __init__(self,nombre):
        self.kilometro = []
        self.gramos = []
        self.kilometro_actual = 0
        self.gramos_actuales = 0
        self.nombre_ave = nombre

    def volar (self,km):
        self.kilometro.append(km)

    def comer(self, gramo):
        self.gramos.append(gramo)

    def CSS (self):
        if len(self.gramos) > 0:            # FORMAS DE DECIR SI LA LISTA ES VACIA: self.gramos != []: o if not self.gramos =[]    
            return sum(self.kilometro) / sum(self.gramos)

        else:
            return None
    
             
    def CSSP(self):
       if len(self.gramos) > 0: 
        return max(self.kilometro) / max(self.gramos)
       
       else:
            return None       

    def CSSV(self):
        if len(self.gramos) > 0: 
            return len(self.kilometro) / len(self.gramos)
        
        else:
            None
    def esta_equilibrio(self):
        return 0.5 <= self.css() <=2 
    
    def nombre(self):
        return self.nombre_ave
    


#Parte2 
# EJERCICIO 2
class Golondrina():
    def __init__ (self,energia,nombre):
         self.energia = energia
         self.nombre_ave = nombre

    def comer_alpiste(self,gramos):
         self.energia = self.energia + 4*gramos
    
    def volar_en_circulos(self):
         self.volar(0)

    def volar(self,kms):
         self.energia -= 10 + kms 

    def esta_debil(self):
         return self.energia <= 10
    
    def saciar(self):
         self.comer_alpiste(100)
    
    def esta_feliz(self):
         return self.energia > 500
    
    def esta_en_equilibrio(self):
         return (self.energia >= 150 and self.energia<= 300)
    
    def nombre(self):
        return self.nombre_ave
    

    
# EJERCICIO 3 
class Ornitologo:
    def __init__(self):
        self.aves = []
             
    def estudiarAve(self,ave):
        self.aves.append(ave)

    def avesEnEstudio(self):
        lista_vacia =[]
        for ave in self.aves:
            lista_vacia.append(ave.nombre())
        return lista_vacia  

    def avesEnEquilibrio(self):
        return [self.aves[i].estaEnEquilibrio() for i in range(len(self.aves))]   
    # recorro la lista de ave y le calculo la long(tiene 4 aves) y voy recocrriendo los indices de la lista.
    # por cada indice, para cada indice en la lista mandas el mensje esta en equilibrio

    #     lista = []
    #     for ave in self.aves:
    #         lista.append(ave.estaEnEquilibrio())
    #         # es lo mismo que la de arriba
    
    def realiazrRutinaSobreAves(self):      #no devuelve
        [self.aves[i].comer(80) for i in range(len(self.aves))]
        [self.aves[i].volar(70) for i in range(len(self.aves))]
        [self.aves[i].comer(10) for i in range(len(self.aves))]


ornitologo = Ornitologo()
golondrina1 = Golondrina(80, "golondrina1")
golondrina2 = Golondrina(75, "golondrina2")
gorrion1 = Gorriones("gorrion1")
gorrion2 = Gorriones("gorrion2")
ornitologo.estudiarAve(golondrina1)
ornitologo.estudiarAve(gorrion1)
ornitologo.estudiarAve(gorrion2)
# ornitologo.realiazrRutinaSobreAves()
# print(ornitologo.avesEnEstudio())   no lo pide pero lo hice porlas
#HAY POLIMORFISMO:saben responder al mensaje esta en equilibrio que manda la clase de ornitologo


#falta instanciar
