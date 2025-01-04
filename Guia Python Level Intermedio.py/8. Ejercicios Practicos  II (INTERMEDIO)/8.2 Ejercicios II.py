#creando una funcion que nos devuelvan los numeros primos emtre 0 y el argumento que pasamos

#crear una funcion que verifique que el numero es primo
def es_primo(num):
#verificamos que el numero pasado no pueda dividirse por ningun numero entre 2 y ese mismo numero -1
    for i in range(2,num-1):
    # si es divisible por alguno retornamos false y termina el bucle
        if num%i == 0: return False
    #si termina el bucle, significa que no fue divisible entonces es primo
    return True

#creamos una funcon que retorne una lista con todos los primos
def primos_hasta(num):
#creamos una lista 
    primos = []
    for i in range (2,num +1):
    #verificamos si el valor es primo
        resultado = es_primo(i)
    #en caso de que sea lo que agregamos a la lista
        if resultado == True: primos.append(i)
    #devolvemos la lista
    return primos 
#creamos el resultado llamando a la funcion y lo mostramos
resultado = primos_hasta(4)

print (resultado)

#forma optimizada en un solo codigo:

def primos_nuevo(num):
  """
  Esta función calcula la lista de números primos menores a un número dado.

  Args:
      num (int): El número límite superior para la lista de primos.

  Returns:
      list: Una lista de números primos menores a 'num'.
  """
  return list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)), range(2, num)))

print(primos_nuevo(15))


'''''
Explicación del código:

def primos_nuevo(num):: Define una función llamada primos_nuevo que recibe un argumento num.

""" ... """: Documentación de la función, que describe su propósito, argumentos y retorno.

return list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)), range(2, num))): Esta línea es la parte central de la función. Vamos a desglosarla paso a paso:

range(2, num): Crea una lista de números desde 2 hasta num (excluyendo num).

filter(lambda x: ... , ...): Aplica un filtro a la lista creada. El filtro se define por la función anónima lambda x: ... que determina si un número x es primo o no.

lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)): Esta función anónima verifica si un número x es primo.
int(x**0.5) + 1: Calcula la raíz cuadrada de x y la redondea al entero más cercano. Se suma 1 para asegurar que se comprueban todos los divisores posibles.

range(2, int(x**0.5) + 1): Crea una lista de números desde 2 hasta la raíz cuadrada de x.
x % i != 0: Verifica si x es divisible por i. Si no es divisible, el resultado es True.

all(...): Devuelve True si todos los elementos en la lista son True. Es decir, si x no es divisible por ningún número en el rango de 2 hasta su raíz cuadrada.

list(...): Convierte el resultado del filtro en una lista.

print(primos_nuevo(15)): Imprime la lista de números primos menores que 15.
'''