import numpy as np

# Crear arrays básicos:

# Un array unidimensional con los números del 1 al 10

array_1d = np.array([1,2,3,4,5,6,7,8,9,10])
print("Array 1D (1-10):")
print(array_1d)
print(f"Forma: {array_1d.shape}, Dimensiones: {array_1d.ndim}, Tipo: {array_1d.dtype}\n")

# Array 3x3 de ceros
array_ceros = np.zeros((3, 3))
print("Array 3x3 de ceros:")
print(array_ceros)
print(f"Forma: {array_ceros.shape}, Dimensiones: {array_ceros.ndim}, Tipo: {array_ceros.dtype}\n")

# Array 2x4 de unos

array_unos = np.ones((2, 4))
print("Array 2x4 de unos:")
print(array_unos)
print(f"Forma: {array_unos.shape}, Dimensiones: {array_unos.ndim}, Tipo: {array_unos.dtype}\n")

# Un array con los números pares del 2 al 20 (existe una función para hacerlo)

array_pares = np.arange(2,21,2)
print("Array numeros pares 2-20:")
print(array_pares)
print(f"Forma: {array_pares.shape}, Dimensiones: {array_pares.ndim}, Tipo: {array_pares.dtype}\n")

# Crear arrays con valores específicos:

# Una matriz identidad de tamaño 4x4 (existe una función para hacerlo)

matriz = np.eye(4)
print("Matriz 4x4")
print(matriz)
print(f"Forma: {matriz.shape}, Dimensiones: {matriz.ndim}, Tipo: {matriz.dtype}\n")

# Un array con valores del 0 al 1 en 5 pasos iguales (existe una función para hacerlo)

array_iguales = np.linspace(0, 1, 5)
print("array con valores del 0 al 1 en 5 pasos iguales")
print(array_iguales)
print(f"Forma: {array_iguales.shape}, Dimensiones: {array_iguales.ndim}, Tipo: {array_iguales.dtype}\n")

# Un array con 6 valores aleatorios entre 0 y 10
array_aleatorios = np.random.randint(0, 10, size=6)
print("array con 6 valores aleatorios entre 0 y 10")
print(array_aleatorios)
print(f"Forma: {array_aleatorios.shape}, Dimensiones: {array_aleatorios.ndim}, Tipo: {array_aleatorios.dtype}\n")

# Realizar operaciones básicas:

# Multiplicar el primer array por 2
multiplicar = (array_1d)*2 
print("Array 1D (1-10) x 2:")
print(multiplicar)
print(f"Forma: {multiplicar.shape}, Dimensiones: {multiplicar.ndim}, Tipo: {multiplicar.dtype}\n")

# Sumar 5 a todos los elementos del array de ceros

sumar = array_ceros+5
print("Array suma 5:")
print(sumar)
print()

# Calcular la suma total de todos los elementos del array de unos

calcular_suma_elementos = np.sum(array_unos)
print("suma total de todos los elementos del array de unos:")
print(calcular_suma_elementos)
print()