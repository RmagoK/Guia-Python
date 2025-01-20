import csv

with open ("Guia-Python-Level-Semi-Avanzado.py/archivoss/prueba.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)
