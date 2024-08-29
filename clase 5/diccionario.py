# Diccionario vacío
mi_diccionario = {}

# Diccionario con algunos elementos
diccionario_contactos = {
    'Juan': 'juan@example.com',
    'Ana': 'ana@example.com',
    'Luis': 'luis@example.com'
}

# Diccionario con diferentes tipos de claves
diccionario_mixto = {
    1: 'uno',
    'dos': 2,
    (3, 4): 'tres y cuatro'
}

print("Diccionario de contactos:", diccionario_contactos)
print("Diccionario con claves mixtas:", diccionario_mixto)

# Modificar un valor existente
diccionario_contactos['Ana'] = 'nuevo_ana@example.com'
print("Diccionario después de modificar el email de Ana:", diccionario_contactos)

# Añadir un nuevo par clave-valor
diccionario_contactos['Carlos'] = 'carlos@example.com'
print("Diccionario después de añadir a Carlos:", diccionario_contactos)

# Eliminar un elemento con pop()
email_eliminado = diccionario_contactos.pop('Luis', 'No encontrado')
print("Email eliminado:", email_eliminado)
print("Diccionario después de eliminar a Luis:", diccionario_contactos)

# Eliminar el último par clave-valor añadido con popitem()
ultimo_eliminado = diccionario_contactos.popitem()
print("Último par eliminado:", ultimo_eliminado)
print("Diccionario después de popitem():", diccionario_contactos)

# Limpiar el diccionario
diccionario_contactos.clear()
print("Diccionario después de limpiar:", diccionario_contactos)

# Reconstruir diccionario para iterar
diccionario_contactos = {
    'Juan': 'juan@example.com',
    'Ana': 'nuevo_ana@example.com',
    'Carlos': 'carlos@example.com'
}

# Iterar sobre las claves
print("Claves en el diccionario:")
for clave in diccionario_contactos.keys():
    print(clave)

# Iterar sobre los valores
print("\nValores en el diccionario:")
for valor in diccionario_contactos.values():
    print(valor)

# Iterar sobre pares clave-valor
print("\nPares clave-valor en el diccionario:")
for clave, valor in diccionario_contactos.items():
    print(f"{clave}: {valor}")
