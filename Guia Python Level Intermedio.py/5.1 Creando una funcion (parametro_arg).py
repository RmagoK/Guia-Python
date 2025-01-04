#Forma NO optima de sumar valores
def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados
    
resultado = suma([5,1,5,32,43,2325,235,32,423])
# print(resultado)
    
#Forma No tan optima para sumar valores utilizando el parametro ARGS

def suma (nombre,*numeros):
    return f"{nombre}, la suma total es:, {sum (numeros)}"

resultado = suma ("rosheed",6,8,9,6,5,2)
# print (resultado)

#Forma optima para sumar valores utilizando el parametro ARGS

def suma_total (numeros):
    return sum([*numeros])

resultado = suma_total ([8,5,7,5,2])     
print (resultado)