#Van entre paréntesis, en vez de corchete como en las listas
#No append, extend, remove
mitupla=("Juan", 13, 1, 1995)
print(mitupla[1])

#Convertir una tupla en lista
mitupla=("Juan", 13, 1, 1995)
milista=list(mitupla)
print(milista)

#Convertir una lista en tupla
milista=["Juan", 13, 1, 1995]
mitupla=tuple(milista)
print(mitupla)

#Para ver si un elemento se encuentra dentro de la tupla
milista=["Juan", 13, 1, 1995]
mitupla=tuple(milista)
print("Juan" in mitupla)

#Cuántas veces se encuentra un elementro dentro de la tupla
milista=["Juan", 13, 1, 1995]
mitupla=tuple(milista)
print(mitupla.count(13))

#Cuántos elementos hay en la tupla
milista=["Juan", 13, 1, 1995]
mitupla=tuple(milista)
print(len(mitupla))

#Tupla unitaria
mitupla=("Juan",)
print(len(mitupla))

#Empaquetado de tupla: escribir una tupla sin parentesis
mitupla="Juan", 13, 1, 1995
print(mitupla)

#Desempaquetado de tupla
mitupla=("Juan", 13, 1, 1995)
nombre, dia, mes, agno=mitupla
print(nombre)
print(dia)
print(agno)
print(mes)
