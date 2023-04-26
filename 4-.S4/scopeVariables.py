#alcance de una variable

#alcance globalporque no esta dentro de una estructura
variable_global = "se puede acceder desde todo el documento"

#funcion para identificar variable local
#def nombre_metodo(parametros_entrada)

def suma(a,b):
    suma_valores = a + b
    if True:
        print(suma_valores)
    return suma_valores

print(suma(2,1))
print(variable_global)

