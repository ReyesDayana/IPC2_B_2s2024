# Abrir un fichero para leer
try:
    archivo_lectura = open('ejemplo.txt', 'r')
    print("Archivo abierto en modo lectura")
except FileNotFoundError:
    print("El archivo no existe")

# Abrir un fichero para escribir (si no existe, se crea)
archivo_escritura = open('escritura.txt', 'w')
print("Archivo abierto en modo escritura")

# Abrir un fichero para añadir (agregar texto al final)
archivo_adicion = open('adicion.txt', 'a')
print("Archivo abierto en modo adición")

archivo_lectura.close()
archivo_escritura.close()
archivo_adicion.close()

with open('escritura.txt', 'w') as archivo:
    archivo.write("Esta es una línea escrita en el archivo.\n")
    archivo.write("Aquí va otra línea.")

with open('escritura.txt', 'r') as archivo:
    contenido = archivo.read()
    print("Contenido del archivo 'escritura.txt':")
    print(contenido)

#Lectura y Escritura
# Abrir el fichero para lectura y escritura
with open('escritura.txt', 'r+') as archivo:
    # Leer el contenido actual
    contenido = archivo.read()
    print("Contenido inicial del archivo:")
    print(contenido)

    # Escribir nuevas líneas
    archivo.write("\nNueva línea agregada al final.")

    # Volver a leer para verificar
    archivo.seek(0)  # Volver al inicio del archivo
    contenido_actualizado = archivo.read()
    print("\nContenido actualizado del archivo:")
    print(contenido_actualizado)