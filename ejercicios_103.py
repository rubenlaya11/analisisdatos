import numpy as np
import pandas as pd
# Crear arrays de datos de ventas:

# Crear un array 2D que represente las ventas mensuales de 3 productos durante 4 meses
ventas = np.random.randint(100, 1001,size=(3, 4))
print("Matriz de ventas (Productos x Meses):")
print(ventas)

# Los datos deben ser valores aleatorios entre 100 y 1000
ventas = np.random.randint(100, 1001, size=(3, 4))
print("Matriz de ventas (Productos x Meses):")
print(ventas)

# Crear un array 1D con los nombres de los productos: "Producto A", "Producto B", "Producto C"
print("Productos: ")
productos = np.array(["Producto A", "Producto B", "Producto C"])
print(productos)

# Crear un array 1D con los nombres de los meses: "Enero", "Febrero", "Marzo", "Abril"
print("Meses: ")
meses = np.array(['Enero', 'Febrero', 'Marzo', 'Abril'])
print(meses)

# Análisis estadístico básico:

# Calcular la media de ventas por producto (por fila)
media_ventas = np.mean(ventas, axis=1)
print("Calcular media ventas: ")
for i, producto in enumerate(productos):
    print(f"{producto}: {media_ventas[i]:2f}")

# Calcular la media de ventas por mes (por columna)
media_ventas_mes = np.mean(ventas, axis=0)
print("calcular media ventas por columna: ")
for i, producto in enumerate(productos):
    print(f"{producto}: {media_ventas_mes[i]:2f}")
    print([i])
    print(producto)

# Desviación estándar por producto
std_por_producto = np.std(ventas, axis=1)
print("Desviación estándar por producto:")
for i, producto in enumerate(productos):
    print(f"{producto}: {std_por_producto[i]:.2f}")
print()

# Encontrar el producto con mayor venta total
ventas_totales = np.sum(ventas, axis=1)
max_producto = productos[np.argmax(ventas_totales)]
print("Producto con mayor venta:")
print(f"{max_producto} con {np.max(ventas_totales)} ")    

# Encontrar el mes con menor venta total
ventas_totales_por_mes = np.sum(ventas, axis=0)
mes_menor_ventas = meses[np.argmin(ventas_totales_por_mes)]
print(f"El mes con menor ventas es {mes_menor_ventas} con {np.min(ventas_totales_por_mes)}")

# Filtrado y selección avanzada:

# Filtrar solo las ventas mayores a 500
ventas_altas = ventas[ventas >= 500]
print(f"Ventas mayores a 500: {ventas_altas}")

# Encontrar todos los meses donde el Producto A tuvo ventas superiores a la media
media_ventas_producto_a = np.mean(ventas[0, :])
meses_producto_a = meses[ventas[0, :] > media_ventas_producto_a]
ventas_altas_producto_a = ventas[0, ventas[0, :] > media_ventas_producto_a]
print(ventas)
print(media_ventas_producto_a)
print(f"{meses_producto_a} con {ventas_altas_producto_a}")
# Crear una máscara booleana para ventas entre 300 y 700
mascara_booleana = (ventas > 300)  & (ventas < 700)
print(mascara_booleana)
# Mostrar las ventas que cumplen con la máscara
# print(ventas[mascara_booleana])
# Operaciones matemáticas:

# Calcular el porcentaje que representa cada producto del total de ventas
ventas_productos = np.sum(ventas, axis=1)
porcentaje_producto = (ventas_productos/np.sum(ventas))*100
for i, producto in enumerate(productos):
    print(porcentaje_producto[i])

# Normalizar las ventas (restar media y dividir por desviación estándar)
normalizar_ventas = (np.sum(ventas) - np.mean(ventas))/np.std(ventas)
print(normalizar_ventas)

# Calcular la correlación entre las ventas de Producto A y Producto B
correlacion_productos_ab = np.corrcoef(ventas[0,:], ventas[1, :])[0,1]
print(correlacion_productos_ab)
# Crear un array con las ventas acumuladas por mes
ventas_acumuladas = np.cumsum(ventas, axis=1)
# Manipulación de arrays:

# Transponer la matriz de ventas

ventas_traspuestas = ventas.T
print("traspuestas")
print(ventas_traspuestas)
# Aplanar el array de ventas y calcular estadísticas

# Reshape el array a diferentes formas (2x6, 6x2, 1x12)
reformar_array = ventas.reshape(2,6)
print(reformar_array)
# Concatenar el array de ventas con una fila adicional de totales