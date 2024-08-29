# Crear una tupla vacía
tupla_vacia = ()

# Crear una tupla con elementos
tupla_uno = (1, 2, 3)

# Crear una tupla con diferentes tipos de datos
tupla_mixta = (1, "dos", 3.0, [4, 5])

# Crear una tupla sin paréntesis (empaquetado de tupla)
tupla_sin_parentesis = 1, 2, 3

print("Tupla vacía:", tupla_vacia)
print("Tupla con números:", tupla_uno)
print("Tupla mixta:", tupla_mixta)
print("Tupla sin paréntesis:", tupla_sin_parentesis)

# Acceder al primer elemento de la tupla
primer_elemento = tupla_uno[0]
print("Primer elemento de tupla_uno:", primer_elemento)

# Acceder al último elemento usando índices negativos
ultimo_elemento = tupla_uno[-1]
print("Último elemento de tupla_uno:", ultimo_elemento)

# Acceder a una porción de la tupla (slicing)
sub_tupla = tupla_uno[1:3]
print("Sub-tupla de tupla_uno (índices 1 a 2):", sub_tupla)

# Intento de modificar un elemento (esto generará un error)
try:
    tupla_uno[0] = 100  # Esto lanzará un TypeError
except TypeError as e:
    print(f"Error: {e}")

#  concatenar tuplas para crear una nueva
nueva_tupla = tupla_uno + (4, 5)
print("Nueva tupla después de concatenar:", nueva_tupla)

# Desempaquetado de tupla en variables
a, b, c = tupla_uno
print("Valores desempaquetados:", a, b, c)

# Desempaquetado parcial
x, y, *resto = (1, 2, 3, 4, 5)
print("Desempaquetado parcial:", x, y, resto)

# Obtener la longitud de una tupla
longitud_tupla = len(tupla_uno)
print("Longitud de tupla_uno:", longitud_tupla)

# Obtener el valor máximo y mínimo (en tuplas de números)
tupla_numeros = (5, 1, 8, 3)
valor_maximo = max(tupla_numeros)
valor_minimo = min(tupla_numeros)
print("Valor máximo en tupla_numeros:", valor_maximo)
print("Valor mínimo en tupla_numeros:", valor_minimo)

# Convertir una lista a tupla
lista = [1, 2, 3]
tupla_convertida = tuple(lista)
print("Lista convertida a tupla:", tupla_convertida)

# Comprobar la existencia de un elemento en una tupla
existe = 2 in tupla_uno
print("¿Existe el valor 2 en tupla_uno?:", existe)
