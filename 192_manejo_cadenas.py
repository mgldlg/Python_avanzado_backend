# manejo de cadenas

# Dividir una cadena split()
cadena = "Hola Mundo"
palabras = cadena.split()
print(palabras)

# Buscar con find
posicion = cadena.find("Mundo") # devolver el valor de 5
print(f"Posición de la cadena Mundo: {posicion}")

# Reemplazar con replace
nueva_cadena = cadena.replace("Mundo","Amigo")
print(f"Nueva cadena reemplaza: {nueva_cadena}")

# Multiplicación de cadenas
cadena = "Hola "
resultado_multiplicacion_cadenas = cadena * 5
print(f"Resultado multiplicación de cadenas: {resultado_multiplicacion_cadenas}")

# Strip - limpiar una cadena

cadena = "...Hola Mundo....."
cadena_limpia = cadena.strip(".")
print(f"Cadena limpia de catacteres al inicio y al final: {cadena_limpia}")