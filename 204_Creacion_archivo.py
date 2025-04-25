# Crear un archivo
nombre_archivo = nombre_archivo = r"C:/Workspace/Python_avanzado_backend/Universidad_Python\204. mi_archivo.txt" # En el ejemplo sólo viene "mi_archivo.txt", pero al guardar lo hace en la raíz de Workspace. Al añadir "r" y la ruta se guarda en la ruta indicada.

# Abrir el archivo en modo escritura ("w")
archivo = open(nombre_archivo, "w")
archivo.write("Hola cómo estás\n")
archivo.write("estoy agregando información al archivo\n")
archivo.close()

print(f"Se creó el archivo: {nombre_archivo}")

# Crear un archivo utilizando la instrucción with
nombre_archivowith = r"C:/Workspace/Python_avanzado_backend/Universidad_Python\204. mi_archivowith.txt"

# Abrir el archivo en modo escritura con with  ("w")
with open(nombre_archivowith, "w") as archivowith:
    archivowith.write("Hola cómo estás\n")
    archivowith.write("estoy agregando información al archivo con with.\n")

print(f"Se creó el archivo: {nombre_archivowith}")
cvzxxz