'''
ciclo for 

se utiliza para recorridos, tuplas, 
diccionarios, set, string
se utliza metodo range() para ibtener un rango
se utiliza el metodo len() para obtener el tamaño

'''

#indice o donde se encuentra el elemento, paret desde 0
#        0, 1, 2, 3, 4, 5 desde 0 a n-1
lista = [1, 2, 3, 4, 5, 6] #lista con elementos

#recorreudno o conocuendio los elementos de la lista

for item in lista:
    print("recorriendo el elemento de la lista", item)
    
for item in range(len(lista)):
    print("Recorriendo el indice de la lista", item)
    print("recorriendo el indice de la lista", lista(item))

#recorriendo o conociuendo indice de lista
for item in lista:
    print("recorriendo el indice de la lista", lista.index(item))
    
#diccionario 

diccionario = {"a": 1, "b":2, "c":3, "d":4, "e":5}

#obteniendo de una key

for item in diccionario: 
    print("ibteniendo el valor de la clave")

#obteniendo value de una clave 
for item in diccionario:
    print("obteniendo el valor", diccionario(item))

for item in diccionario:
    print("obteniendo el valor", item)
    
# obteniendo solo los keys i clave
for item in diccionario.item():
    print("obteniendo el elemento con clave;valor".item)
