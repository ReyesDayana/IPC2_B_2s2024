import re

# Buscar una palabra en una cadena
patron = r"hola"
cadena = " mundo"

resultado = re.search(patron, cadena)
if resultado:
    print("Se encontró el patrón")
else:
    print("No se encontró el patrón")

# Buscar si una cadena empieza con una palabra específica
patron_inicio = r"^hola"
cadena = "hola mundo"

if re.search(patron_inicio, cadena):
    print("La cadena empieza con 'hola'")
else:
    print("La cadena no empieza con 'hola'")

# Buscar si una cadena termina con una palabra específica
patron_final = r"mundo$"
if re.search(patron_final, cadena):
    print("La cadena termina con 'mundo'")
else:
    print("La cadena no termina con 'mundo'")

# Encontrar todas las palabras en una cadena
patron = r"\b\w+\b"  # \b es un límite de palabra, \w+ es una palabra
cadena = "El sol brilla y el viento sopla."

resultados = re.findall(patron, cadena)
print("Palabras encontradas:", resultados)

# Dividir una cadena en palabras
patron = r"\s+"  # \s+ coincide con uno o más espacios en blanco
cadena = "Esta es una cadena con    espacios en blanco"

partes = re.split(patron, cadena)
print("Partes de la cadena:", partes)

# Sustituir todas las ocurrencias de una palabra por otra
patron = r"mundo"
cadena = "Hola mundo, mundo, mundo!"
nueva_cadena = re.sub(patron, "Python", cadena)

print("Cadena después de la sustitución:", nueva_cadena)

# Capturar el nombre y el dominio de un correo electrónico
patron = r"(\w+)@(\w+\.\w+)"
cadena = "correo@example.com"

resultado = re.search(patron, cadena)
if resultado:
    nombre = resultado.group(1)
    dominio = resultado.group(2)
    print(f"Nombre: {nombre}, Dominio: {dominio}")
else:
    print("No se encontró el patrón")

# Buscar una palabra independientemente de mayúsculas o minúsculas
patron = r"python"
cadena = "Me encanta Python y python."

resultados = re.findall(patron, cadena, re.IGNORECASE)
print("Coincidencias encontradas:", resultados)

# Validar un número de teléfono (formato: XXX-XXX-XXXX)
patron = r"^\d{3}-\d{3}-\d{4}$"
telefono = "123-456-7890"

if re.match(patron, telefono):
    print("Número de teléfono válido")
else:
    print("Número de teléfono inválido")

# Compilar un patrón y usarlo varias veces
patron_compilado = re.compile(r"\d{3}-\d{3}-\d{4}")

telefonos = ["123-456-7890", "987-654-3210", "1234567890"]

for telefono in telefonos:
    if patron_compilado.match(telefono):
        print(f"{telefono} es válido")
    else:
        print(f"{telefono} no es válido")