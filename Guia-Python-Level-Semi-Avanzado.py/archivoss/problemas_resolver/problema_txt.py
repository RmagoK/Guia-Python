#MI lista, una con nombres y otra con apellidos

Nombres = ["Rosheed", "Carlos", "Alejandro", "Jonathan"]
Apellidos = ["Mago", "Silva", "Jimenez", "Centeno"]

#Registrar esta informacion en un TXT de forma optima

with open("nombres_y_apellidos.txt","w") as arch:
    arch.writelines("los datos son: \n")
    [arch.writelines(f"nombre: {n}\n Apellido {a}\n ---------------------") for n,a in zip(Nombres, Apellidos)]

print (arch)