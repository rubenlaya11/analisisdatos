import pandas as pd
# Crear un DataFrame de ejemplo:

# Crear un DataFrame con información de estudiantes que contenga las siguientes columnas:
# Nombre: nombres de 5 estudiantes
# Edad: edades entre 18 y 25 años
# Nota_Matematicas: notas entre 0 y 10
# Nota_Historia: notas entre 0 y 10
# Ciudad: ciudades de origen

data = {
    'Nombre' : ['Paco', 'Jesús', 'Yaiza', 'Rubén', 'Xabier'],
    'Edad' : [23, 25, 22, 25, 18],
    'Nota_Matematicas' : [3.4, 6.3, 10, 8, 3],
    'Nota_Historia' : [3, 6, 8, 5, 1],
    'Ciudad' : ['Lima', 'Jaen', 'Moaña', 'Pontevedra', 'Meis']
}

df = pd.DataFrame(data)
print("DataFrame creado: ")
print(df)
print(f"\nForma: {df.shape}")
print(f"Columnas: {list(df.columns)}")
print(f"Tipos de datos:\n{df.dtypes}")

df.to_csv('alumnos_teis.csv', index=False)
print("Archivo CSV creado")

# Exploración básica de datos:

# Mostrar las primeras 4 filas del DataFrame
df_csvleido = pd.read_csv('alumnos_teis.csv')
print(df_csvleido.head(4))

# Mostrar información general del DataFrame (tipos de datos, valores nulos)
print("Información general: ")
print(df_csvleido.info()) 

# Mostrar estadísticas descriptivas de las columnas numéricas
print("estadísticas descriptivas: ")
print(df_csvleido.describe())

# Mostrar el número total de estudiantes
print("Número total de estudiantes: ")
print(len(df_csvleido))

num_estudiantes = df_csvleido['Nombre'].__len__()
print(num_estudiantes)

# Selección y filtrado:

# Seleccionar solo las columnas Nombre y Nota_Matematicas

print(f"{df_csvleido[['Nombre', 'Nota_Matematicas']]}")

# Filtrar estudiantes con nota de matemáticas mayor a 7
print("Estudiantes con nota +7: ")
estudiantes_notable = df_csvleido[df_csvleido['Nota_Matematicas'] > 7]
print(estudiantes_notable)
# Filtrar estudiantes menores de 22 años
print("estudiantes menores de 22 años: ")
estudiantes_menores = df_csvleido[df_csvleido['Edad'] < 22]
print(estudiantes_menores)
# Mostrar el estudiante con la nota más alta en historia
print("estudiante con la nota más alta en historia")
estudiante_mejor_nota_historia = df_csvleido.loc[df_csvleido['Nota_Historia'].idxmax()]
print(estudiante_mejor_nota_historia)

# Operaciones básicas:

# Calcular la nota media de matemáticas

print("Cálculo de la nota media de matemáticas: ")
nota_media = df_csvleido['Nota_Matematicas'].mean()
print(nota_media)

# Calcular la nota media de historia
print("Cálculo de la nota media de historia: ")
nota_media_historia = df_csvleido['Nota_Historia'].mean()
print(nota_media_historia)

# Crear una nueva columna Nota_Media con el promedio de ambas asignaturas
df_csvleido['NotaMedia'] = (df_csvleido['Nota_Matematicas'] + df_csvleido['Nota_Historia'])/2
print(df_csvleido)

# Ordenar el DataFrame por nota media de mayor a menor
print("Ordenar DF por notamedia de mayor a menor")
print(df_csvleido.sort_values('NotaMedia', ascending=False))


