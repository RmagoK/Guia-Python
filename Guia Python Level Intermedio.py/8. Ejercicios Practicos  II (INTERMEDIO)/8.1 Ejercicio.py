#Ejercicio 1

#Hoy falto el profesor de clases y los chicos se unieron para armar la suya propia, uno de los alumnos sera el profesor y el otro el asistente:


#1 alumno es profesor
#2 alumno es asistente

# A = Pedir la edad de los companeros que vinieron hoy a clases y ordenar los datos de menor a mayor

# B = El mayor es el profesor y el menor es el asistente: quien es quien


#Funcion para pedir el nombre y le edad de los companeros que asistieron en clase

def obtener_companeros(cantidad_de_companeros):
    companeros = []

#Ejecutamos un for para pedir informacion de los companeros
    for i in range (cantidad_de_companeros):
        nombre = input ("ingrese el nombre del companero: ")
        edad = int (input ("ingrese la edad del companero: "))
        companero = (nombre, edad)

    #agregando la informacion a la lista
        companeros.append (companero)

    #ordenando de menor a mayor segun la edad
    companeros.sort (key= lambda x:x[1])

    #companeros(x) devuelve una tupla con (nombre,edad) y despues accedemos al nombre para definir al asistente y al profesor
    asistente = companeros[0][0] 
    profesor = companeros [-1][0]

    #retornamos una tupla
    return asistente,profesor

#desempaquetamos lo que nos retorna la funcion
asistente, profesor = obtener_companeros(5)

#mostramos resultado
print(f"EL asistente es: {asistente}, y el profesor es: {profesor}")