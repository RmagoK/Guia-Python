with open("Guia-Python-Level-Semi-Avanzado.py/archivoss/texto.txt","a") as archivo:

    #agregando separador entre nuevos guardados
    
    archivo.write("\n")
    #creando varias lineas con for
    for i in range(5):
    #agregando lineas
        archivo.write(f"linea {i+1} agregada \n")
        


    