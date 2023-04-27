"""
CUE: TIPOS DE DATOS Y SENTENCIAS
REBOUND EXERCISES: CREACIÓN DE VARIABLES CON DIFERENTES TIPOS DE DATOS.
Para resolver este ejercicio, anteriormente debe haber revisado la lectura y los videos del CUE:
Tipos de datos y sentencias.
EJERCICIO
Requerimos crear una variable con el número 8, una con el número 10.5, y una con la palabra
“ejercicio”. Luego, crear un set que contendrá cada una de las variables que creamos, y será
asignado a una variable.
A continuación, crearemos una lista que contendrá el set creado anteriormente, y una variable con
el valor lógico False. Esta lista la asignaremos a una variable que luego imprimiremos en pantalla.
"""
# Creamos las variables
num1 = 8
num2 = 10.5
palabra = "ejercicio"

# Creamos el set
mi_set = {num1, num2, palabra}

# Creamos la lista con el set y la variable lógica False
mi_lista = [mi_set, False]

# Imprimimos la lista en pantalla
print(mi_lista)
