with open("Guia-Python-Level-Semi-Avanzado.py/archivoss/texto.txt","w") as archivo:

    #sobreescribiendo el archivo
    #archivo.write("Vamos bien")
    archivo.writelines([" Vamosbien 2.0 \n"," vamos bien 3.0 \n"])

    #agregando dos lineas mas
    archivo.writelines([" Vamosbien 3.1 \n"," vamos bien 3.2 \n"])
    