# Hacer un programa que cuente del 1 al 100 inclusive e imprima los números que son divisibles por 2 y por 5.

for i in range(1, 101):
    if not (i % 2) and not (i % 5):
        print(i)