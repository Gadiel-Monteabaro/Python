# Crea una lista de números desordenados y ordénala en orden ascendente y descendente.
numeros = [3, 5, 8, 7, 4, 9, 6]
              
for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] > numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]

print(numeros)

for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] < numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]

print(numeros)