#Abriendo el archivo con with Open
with open("Guia-Python-Level-Semi-Avanzado.py/archivoss/texto.txt") as archivo:
    #leemos el archivo 
    Contenido = archivo.read()

print(Contenido)

#No es necesario cerrarlo con with open
