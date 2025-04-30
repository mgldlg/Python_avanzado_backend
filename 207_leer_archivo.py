print("*** Leer Archivo con Python ***")

nombre_archivo = r"c:\Workspace\Python_avanzado_backend\206. mi_archivo.txt"

# Leer un archivo usando el método readlines
with open(nombre_archivo, "r") as archivo:
    # Leer todas las líneas del archivo
    # print(archivo.readlines())    # Quitar la almohadilla de esta línea si eliminamos el código que sigue.
    lineas = archivo.readlines()
    for linea in lineas:
        # print(linea)    # Poner la almohadilla en esta línea o la siguente dependiendo de lo que queramos ejecutar.
        print(linea.strip())  # Elimina el salto de línea al final de cada línea

# Leer el contenido del archivo usando read
print("Leyendo el contenido con el método read")
with open(nombre_archivo, "r") as archivo:
    print(archivo.read())   # Poner la almohadilla en esta línea o la siguente dependiendo de lo que queramos ejecutar.
    print(archivo.read().strip())  # Elimina el salto de línea al final de cada línea
