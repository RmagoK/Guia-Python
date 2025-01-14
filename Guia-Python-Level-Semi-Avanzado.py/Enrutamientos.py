#Si el modulo estuviera dentro de una carpeta en la misma ruta se encuentra asi:
import funciones_buenas.Modulo_saludar as M

print (M.saludar("Rosheed"))

#Si el modulo se encuentra fuera de la carpeta 

import sys

#varios modulos nativos de python
print(sys.builtin_module_names)

#ruta del modulo a cual buscar
print(sys.path)

sys.path.append("Mi-crecimiento_en_python-master/Guia Python Level Semi Avanzado.py")

#luego podemos volver a importar el modulo de forma normal con import  