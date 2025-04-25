print("*** Función sum y next ***")

lista = [1, 2, 3, 4, 5]

# Suma de todos los elementos
resultado = sum(lista)
print(f" Resultado de la suma: {resultado}")

# Podemos proprocionar un valor inicial
resultado = sum(lista, 20)
print(f" Resultado de la suma con valor inicial de 20: {resultado}")

# La función next
iterador = iter(lista)

# Obtenemos el próximo elemento del iterador usando la función next
print(f" El siguiente elemento del iterador es: {next(iterador)}")
print(f" El siguiente elemento del iterador es: {next(iterador)}")
print(f" El siguiente elemento del iterador es: {next(iterador)}")
print(f" El siguiente elemento del iterador es: {next(iterador)}")
print(f" El siguiente elemento del iterador es: {next(iterador)}")
print(f" El siguiente elemento del iterador es: {next(iterador)}")