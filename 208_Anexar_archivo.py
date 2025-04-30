print("*** Anexar información Archivo ***")

nombre_archivo = r"c:\Workspace\Python_avanzado_backend\206. mi_archivo.txt"

with open(nombre_archivo, "a") as archivo:
    # EAnexar información al archivo
    archivo.write("\nAnexando información ... \n")
    archivo.write("Saliendo de anexar información...\n")

print("Se ha anexado información al archivo {nombre_archivo}")