amigos = ['Ana', 'Monica', 'José', 'Camila', 'Raquel', 'Matías']

# Devuelve la posición (el index, un número) del amigo “Matías”.
print("La posicion de Matías es ", amigos.index('Matías'))

# Devuelve la misma lista pero añadiendo los amigos de la infancia “Ivana” y “Andrés” como otra lista.
amigosInfancia = ["Ivana", "Andres"]
amigos.extend(amigosInfancia)

# Agrega un nuevo amigo “María” y devuelve el nro de amigos
amigos.append("María")
print(len(amigos))

# Elimina el último elemento amigo y devuelve el nombre del amigo eliminado
amigoEliminado = amigos.pop()
print("El amigo eliminado es ", amigoEliminado)

# Devuelve un arreglo ordenado alfabéticamente
amigos.sort()
print("Amigos ordenados alfabeticamente ", amigos)


friends = ['Ana', 'Monica', 'José', 'Camila',
           'Raquel', 'Matías', ['Gadiel', 'Melisa']]

countFriends = 0
for i in friends:
    if (type(i) == list):
        for j in i:
            countFriends += 1
            break

    countFriends += 1

print(countFriends)
