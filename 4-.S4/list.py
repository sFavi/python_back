#listas en python 

lista = [1,2,3,4]
lista_diferentes_valores = [1,"2",3,"4", True, False]

print(lista_diferentes_valores)


#para acceder a los valores de un arreglo utilizan los indes
#0 a n-1 pero también pueden ser nagativos

print(lista[0])
print(lista[-1])

#algunos metodos de las listas
#agregar, anexar valor
#nombre.append()
lista.append(5)
print(lista)


#remove
lista.remove(5)
print(lista)

a = lista.pop(1)
print(a)
print(lista)


lista.insert(1,2)
print(lista)

indice =lista.index(2)
print(indice)

#ordena los elementos dentro de la lista
lista.sort()