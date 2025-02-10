# colecciones de datos que se almacenan en pares clave-valor
datos_persona = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Córdoba'}

# Cambiar un valor
datos_persona['nombre'] = 'Gadiel'

# Acceder a un valor
nombre = datos_persona['nombre']
print(nombre)

# Agregar un nuevo par clave-valor
datos_persona['apellido'] = 'Monteabaro'

# Obtener todas las claves
claves = datos_persona.keys()
print(claves)

# Obtener todos los valores
valores = datos_persona.values()
print(valores)

# Obtener todos los items
items = datos_persona.items()
print(items)

# Eliminar un par clave-valor
datos_persona.pop("edad")
print(datos_persona)

# Eliminar todos los pares clave-valor
datos_persona.clear()
print(datos_persona)
