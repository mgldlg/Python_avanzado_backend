print("*** Funciones Lambda ***")

# Funcion cuadrado sin usar lambda
def cuadrado(x):
    return x ** 2

print(f"El cuadrado de 5: {cuadrado(5)}")

# Función lambda (anónima)

cuadrado_lambda = lambda x: x ** 2
print(f"El cuadrado de 2: {cuadrado_lambda(2)}")
print(f"El cuadrado de 2: {cuadrado_lambda(4)}")