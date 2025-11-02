# Hacer un programa que imprima una tabla de multiplicar del 2 al 9 . Cada uno debe mostrar sus valores multiplicados del 1 al 9 inclusive.

for i in range(2, 10):
    print(f"\nTabla de Multiplicar del {i}:")
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
