#Usando open para abrir un archivo con una codificacion universal ETF-8
archivo_LEYENDO = open("Guia-Python-Level-Semi-Avanzado.py/archivoss/texto.txt", encoding="ETF-8")  # Ajustar la ruta si es necesario

#LEER ARCHIVO COMPLETO
#archivo = archivo_sinleer.read()

#Leer una sola linea
#linea = archivo_LEYENDO.readlines()

#Cerrar archivo
archivo_LEYENDO.close()

print(archivo_LEYENDO)
