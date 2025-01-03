#Forma optima de sumar valores
def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados
    
resultado = suma([5,1,5,32,43,2325,235,32,423])
print(resultado)
    
