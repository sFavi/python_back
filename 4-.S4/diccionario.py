#ordenados por clave y valor
#los diccionarios una coleccion de elementos
#declaracion con llaves {} o con la funcion dict()

estudiantes = {
     #clave:valor
     "fulanito": 25, 
     "Maria": 22,
     "Marta": 30,
     "Jose": 35
}

print(estudiantes)

#acceder al valor de una clave
#nombre_diccionario["clave"]
print(estudiantes["fulanito"])

#remover clave de un diccionario

del estudiantes["fulanito"]
print(estudiantes)

claves = estudiantes.keys()
print(claves)

valores = estudiantes.values()
print(valores)

estudiantes.clear()
print(estudiantes)